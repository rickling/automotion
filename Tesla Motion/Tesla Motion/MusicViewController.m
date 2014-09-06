//
//  MusicViewController.m
//  Tesla Motion
//
//  Created by Rick Ling on 9/6/14.
//  Copyright (c) 2014 Rick Ling. All rights reserved.
//

#import <Rdio/Rdio.h>
#import "ConsumerCredentials.h"
#import "MusicViewController.h"

@interface MusicViewController ()

@property (nonatomic, strong) Rdio *rdio;

@end

@implementation MusicViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self setupRdio];
}

#pragma mark - Setup rdio
- (void)setupRdio {
    self.rdio = [[Rdio alloc] initWithConsumerKey:CONSUMER_KEY andSecret:CONSUMER_SECRET delegate:nil];
    [self.rdio preparePlayerWithDelegate:nil];
    NSArray *sources = [NSArray arrayWithObjects:@"t1", @"p1", @"a1", nil];
    [self.rdio.player playSources:sources];
}


- (void)playNextSong {
    //todo: fill in
}

- (void)playPrevSong {
    //todo: fill in
}


#pragma mark - Music View
- (void)setupMusicView {
    
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
