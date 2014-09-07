//
//  MusicViewController.m
//  Tesla Motion
//
//  Created by Rick Ling on 9/6/14.
//  Copyright (c) 2014 Rick Ling. All rights reserved.
//

#import <Rdio/Rdio.h>
#import <MediaPlayer/MediaPlayer.h>
#import "ConsumerCredentials.h"
#import "MediaPlayer/MPVolumeView.h"
#import "MusicViewController.h"
#import "SRWebSocket.h"
#define RDIO_PLAY_PAUSE 0
#define RDIO_NEXT 1
#define RDIO_PREV 2
#define RDIO_VOL_UP 3
#define RDIO_VOL_DOWN 4

@interface MusicViewController ()<SRWebSocketDelegate>

@property (nonatomic, strong) Rdio *rdio;
@property (nonatomic) BOOL isPlaying;
@property (nonatomic, strong) NSMutableArray *topChartSongs;
@property (nonatomic, strong) SRWebSocket *webSocket;
@property (nonatomic, strong) MPVolumeView *volumeView;
@property (nonatomic) float currentVolume;


@end

@implementation MusicViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.isPlaying = NO;
    self.currentVolume = 1.0f;
    [self setupRdio];
    [self setupMusicView];
    [self connectWebSocket];
}

#pragma mark - Setup rdio
- (void)setupRdio {
    self.rdio = [[Rdio alloc] initWithConsumerKey:CONSUMER_KEY andSecret:CONSUMER_SECRET delegate:nil];
    [self.rdio preparePlayerWithDelegate:nil];
    RDAPIRequestDelegate *trackDelegate = [RDAPIRequestDelegate delegateToTarget:self
                                                                    loadedAction:@selector(updateTopChartSongs:didLoadData:)
                                                                    failedAction:@selector(updateTopChartSongs:didFail:)];
    [self.rdio callAPIMethod:@"getTopCharts" withParameters:@{@"type": @"Track"} delegate:trackDelegate];
}

- (void)updateTopChartSongs:(RDAPIRequest *)request didLoadData:(NSDictionary *)data {
    NSArray *topChartArray = (NSArray *)data;
    self.topChartSongs = [[NSMutableArray alloc] init];
    for (NSDictionary *tracks in topChartArray) {
        
        [self.topChartSongs addObject:tracks[@"key"]];
    }
    [self.rdio.player playSources:self.topChartSongs];
    [self playPausePressed];
    
}

- (void)updateTopChartSongs:(RDAPIRequest *)request didFail:(NSError *)error {
    NSLog(@"error: %@", error);
}


#pragma mark - Music View
- (void)setupMusicView {
    self.volumeView = [[MPVolumeView alloc] initWithFrame: self.volumeViewContainer.bounds];
    [self.volumeViewContainer addSubview: self.volumeView];
    [self.playButton addTarget:self action:@selector(playPausePressed) forControlEvents:UIControlEventTouchUpInside];
    [self.nextButton addTarget:self action:@selector(playNextSong) forControlEvents:UIControlEventTouchUpInside];
    [self.prevButton addTarget:self action:@selector(playPrevSong) forControlEvents:UIControlEventTouchUpInside];
}

#pragma mark - Actions
- (void)playPausePressed {
    if (self.isPlaying) {
        [self.rdio.player togglePause];
        [self.playButton setTitle:@"Play" forState:UIControlStateNormal];
        self.isPlaying = NO;
    } else {
        [self.rdio.player play];
        [self.playButton setTitle:@"Pause" forState:UIControlStateNormal];
        self.isPlaying = YES;
    }
    
    sleep(2);
}

- (void)playNextSong {
    [self.rdio.player next];
    sleep(2);
}

- (void)playPrevSong {
    [self.rdio.player previous];
    sleep(2);
}

- (void)increaseVolume {
    UISlider* volumeViewSlider = nil;
    for (UIView *view in [self.volumeView subviews]){
        if ([view.class.description isEqualToString:@"MPVolumeSlider"]){
            volumeViewSlider = (UISlider*)view;
            break;
        }
    }
    if (self.currentVolume < 1.0f) {
        self.currentVolume += 0.1f;
    }
    [volumeViewSlider setValue:self.currentVolume animated:YES];
    [volumeViewSlider sendActionsForControlEvents:UIControlEventTouchUpInside];

}

- (void)decreaseVolume {
    UISlider* volumeViewSlider = nil;
    for (UIView *view in [self.volumeView subviews]){
        if ([view.class.description isEqualToString:@"MPVolumeSlider"]){
            volumeViewSlider = (UISlider*)view;
            break;
        }
    }
    if (self.currentVolume > 0.0f) {
        self.currentVolume -= 0.1f;
    }
    [volumeViewSlider setValue:self.currentVolume animated:NO];
    [volumeViewSlider sendActionsForControlEvents:UIControlEventTouchUpInside];
}

#pragma mark - Web socket
- (void)connectWebSocket {
    self.webSocket.delegate = nil;
    self.webSocket = nil;
    
    NSString *urlString = @"ws://35.2.81.132:9000";
    SRWebSocket *newWebSocket = [[SRWebSocket alloc] initWithURL:[NSURL URLWithString:urlString]];
    newWebSocket.delegate = self;
    
    [newWebSocket open];
}

#pragma mark - SRWebSocketDelegate
- (void)webSocketDidOpen:(SRWebSocket *)newWebSocket {
    self.webSocket = newWebSocket;
    [self.webSocket send:[NSString stringWithFormat:@"Hello from %@", [UIDevice currentDevice].name]];
}

- (void)webSocket:(SRWebSocket *)webSocket didFailWithError:(NSError *)error {
    [self connectWebSocket];
}

- (void)webSocket:(SRWebSocket *)webSocket didCloseWithCode:(NSInteger)code reason:(NSString *)reason wasClean:(BOOL)wasClean {
    [self connectWebSocket];
}

- (void)webSocket:(SRWebSocket *)webSocket didReceiveMessage:(id)message {
    
    NSLog(@"%@", message);
    switch ([message intValue]) {
        case RDIO_PLAY_PAUSE:
            [self playPausePressed];
            break;
        case RDIO_NEXT:
            [self playNextSong];
            break;
        case RDIO_PREV:
            [self playPrevSong];
            break;
        case RDIO_VOL_UP:
            [self increaseVolume];
            break;
        case RDIO_VOL_DOWN:
            [self decreaseVolume];
            break;
    }
}

@end
