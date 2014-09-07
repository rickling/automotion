//
//  MusicViewController.h
//  Tesla Motion
//
//  Created by Rick Ling on 9/6/14.
//  Copyright (c) 2014 Rick Ling. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface MusicViewController : UIViewController

@property (weak, nonatomic) IBOutlet UILabel *songNameLabel;
@property (weak, nonatomic) IBOutlet UILabel *artistNameLabel;
@property (weak, nonatomic) IBOutlet UIButton *playButton;
@property (weak, nonatomic) IBOutlet UIButton *nextButton;
@property (weak, nonatomic) IBOutlet UIButton *prevButton;
@property (weak, nonatomic) IBOutlet UIView *volumeViewContainer;

@property (weak, nonatomic) IBOutlet UIImageView *trackImageView;
@property (weak, nonatomic) IBOutlet UIImageView *circleTrackImageView;

@end
