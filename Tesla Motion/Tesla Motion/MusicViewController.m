//
//  MusicViewController.m
//  Tesla Motion
//
//  Created by Rick Ling on 9/6/14.
//  Copyright (c) 2014 Rick Ling. All rights reserved.
//

#import <Rdio/Rdio.h>
#import "ConsumerCredentials.h"
#import "MediaPlayer/MPVolumeView.h"
#import "MusicViewController.h"

@interface MusicViewController ()

@property (nonatomic, strong) Rdio *rdio;
@property (nonatomic) BOOL isPlaying;
@property (nonatomic, strong) NSMutableArray *topChartSongs;

@end

@implementation MusicViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.isPlaying = NO;
    [self setupRdio];
    [self setupMusicView];
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
    MPVolumeView *myVolumeView = [[MPVolumeView alloc] initWithFrame: self.volumeViewContainer.bounds];
    [self.volumeViewContainer addSubview: myVolumeView];
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
}

- (void)playNextSong {
    [self.rdio.player next];
}

- (void)playPrevSong {
    [self.rdio.player previous];
}


/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
