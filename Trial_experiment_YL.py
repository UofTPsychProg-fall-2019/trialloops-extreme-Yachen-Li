#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Thu Dec  5 15:33:23 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Trial_experiment_Dec5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'file number': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/yachen/Documents/GitHub/Perspective_taking_builder/Trial_experiment_Dec 5.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
textInstruction = visual.TextStim(win=win, name='textInstruction',
    text="Verify the number of dots either from \nyour perspective or from the avatar's\nperspective. Press Q if the number you \nsee matches the number of dots from the\ncued perspective, press P if the number \ndoes not match the number of dots. \n\nPlease respond as fast as you can. Press\nSpace bar to proceed with the task. Let's\ndo some practice!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Key_instruction = keyboard.Keyboard()

# Initialize components for Routine "Blank500ms"
Blank500msClock = core.Clock()
Blankscreen = visual.TextStim(win=win, name='Blankscreen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Practice_trial"
Practice_trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
blank500ms = visual.TextStim(win=win, name='blank500ms',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
perspective = visual.TextStim(win=win, name='perspective',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
blank500 = visual.TextStim(win=win, name='blank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
numberDots = visual.TextStim(win=win, name='numberDots',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
consistent1 = visual.ImageStim(
    win=win,
    name='consistent1', units='norm', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Response_key = keyboard.Keyboard()
total_acc = 0

# Initialize components for Routine "Blank500ms"
Blank500msClock = core.Clock()
Blankscreen = visual.TextStim(win=win, name='Blankscreen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedbacktext2 = visual.TextStim(win=win, name='feedbacktext2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
# update component parameters for each repeat
Key_instruction.keys = []
Key_instruction.rt = []
# keep track of which components have finished
InstructionComponents = [textInstruction, Key_instruction]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstruction* updates
    if textInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInstruction.frameNStart = frameN  # exact frame index
        textInstruction.tStart = t  # local t and not account for scr refresh
        textInstruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInstruction, 'tStartRefresh')  # time at next scr refresh
        textInstruction.setAutoDraw(True)
    
    # *Key_instruction* updates
    waitOnFlip = False
    if Key_instruction.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        Key_instruction.frameNStart = frameN  # exact frame index
        Key_instruction.tStart = t  # local t and not account for scr refresh
        Key_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Key_instruction, 'tStartRefresh')  # time at next scr refresh
        Key_instruction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Key_instruction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Key_instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Key_instruction.status == STARTED and not waitOnFlip:
        theseKeys = Key_instruction.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            Key_instruction.keys = theseKeys.name  # just the last key pressed
            Key_instruction.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textInstruction.started', textInstruction.tStartRefresh)
thisExp.addData('textInstruction.stopped', textInstruction.tStopRefresh)
# check responses
if Key_instruction.keys in ['', [], None]:  # No response was made
    Key_instruction.keys = None
thisExp.addData('Key_instruction.keys',Key_instruction.keys)
if Key_instruction.keys != None:  # we had a response
    thisExp.addData('Key_instruction.rt', Key_instruction.rt)
thisExp.addData('Key_instruction.started', Key_instruction.tStartRefresh)
thisExp.addData('Key_instruction.stopped', Key_instruction.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500ms"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500msComponents = [Blankscreen]
for thisComponent in Blank500msComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank500ms"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500msClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500msClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Blankscreen* updates
    if Blankscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blankscreen.frameNStart = frameN  # exact frame index
        Blankscreen.tStart = t  # local t and not account for scr refresh
        Blankscreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blankscreen, 'tStartRefresh')  # time at next scr refresh
        Blankscreen.setAutoDraw(True)
    if Blankscreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Blankscreen.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Blankscreen.tStop = t  # not accounting for scr refresh
            Blankscreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Blankscreen, 'tStopRefresh')  # time at next scr refresh
            Blankscreen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500msComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500ms"-------
for thisComponent in Blank500msComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Blankscreen.started', Blankscreen.tStartRefresh)
thisExp.addData('Blankscreen.stopped', Blankscreen.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PerspectiveStimlus.xls', selection='0:22'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Practice_trial"-------
    routineTimer.add(5.250000)
    # update component parameters for each repeat
    perspective.setText(Perspective)
    numberDots.setText(NumberDots)
    consistent1.setImage(ImageName)
    Response_key.keys = []
    Response_key.rt = []
    # keep track of which components have finished
    Practice_trialComponents = [fixation, blank500ms, perspective, blank500, numberDots, consistent1, Response_key]
    for thisComponent in Practice_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Practice_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Practice_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *blank500ms* updates
        if blank500ms.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            blank500ms.frameNStart = frameN  # exact frame index
            blank500ms.tStart = t  # local t and not account for scr refresh
            blank500ms.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank500ms, 'tStartRefresh')  # time at next scr refresh
            blank500ms.setAutoDraw(True)
        if blank500ms.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank500ms.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank500ms.tStop = t  # not accounting for scr refresh
                blank500ms.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank500ms, 'tStopRefresh')  # time at next scr refresh
                blank500ms.setAutoDraw(False)
        
        # *perspective* updates
        if perspective.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            perspective.frameNStart = frameN  # exact frame index
            perspective.tStart = t  # local t and not account for scr refresh
            perspective.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(perspective, 'tStartRefresh')  # time at next scr refresh
            perspective.setAutoDraw(True)
        if perspective.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > perspective.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                perspective.tStop = t  # not accounting for scr refresh
                perspective.frameNStop = frameN  # exact frame index
                win.timeOnFlip(perspective, 'tStopRefresh')  # time at next scr refresh
                perspective.setAutoDraw(False)
        
        # *blank500* updates
        if blank500.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            blank500.frameNStart = frameN  # exact frame index
            blank500.tStart = t  # local t and not account for scr refresh
            blank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank500, 'tStartRefresh')  # time at next scr refresh
            blank500.setAutoDraw(True)
        if blank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank500.tStop = t  # not accounting for scr refresh
                blank500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank500, 'tStopRefresh')  # time at next scr refresh
                blank500.setAutoDraw(False)
        
        # *numberDots* updates
        if numberDots.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            numberDots.frameNStart = frameN  # exact frame index
            numberDots.tStart = t  # local t and not account for scr refresh
            numberDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(numberDots, 'tStartRefresh')  # time at next scr refresh
            numberDots.setAutoDraw(True)
        if numberDots.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > numberDots.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                numberDots.tStop = t  # not accounting for scr refresh
                numberDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(numberDots, 'tStopRefresh')  # time at next scr refresh
                numberDots.setAutoDraw(False)
        
        # *consistent1* updates
        if consistent1.status == NOT_STARTED and tThisFlip >= 3.25-frameTolerance:
            # keep track of start time/frame for later
            consistent1.frameNStart = frameN  # exact frame index
            consistent1.tStart = t  # local t and not account for scr refresh
            consistent1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consistent1, 'tStartRefresh')  # time at next scr refresh
            consistent1.setAutoDraw(True)
        if consistent1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > consistent1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                consistent1.tStop = t  # not accounting for scr refresh
                consistent1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(consistent1, 'tStopRefresh')  # time at next scr refresh
                consistent1.setAutoDraw(False)
        
        # *Response_key* updates
        if Response_key.status == NOT_STARTED and t >= 3.25-frameTolerance:
            # keep track of start time/frame for later
            Response_key.frameNStart = frameN  # exact frame index
            Response_key.tStart = t  # local t and not account for scr refresh
            Response_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_key, 'tStartRefresh')  # time at next scr refresh
            Response_key.status = STARTED
            # keyboard checking is just starting
            Response_key.clock.reset()  # now t=0
            Response_key.clearEvents(eventType='keyboard')
        if Response_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_key.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Response_key.tStop = t  # not accounting for scr refresh
                Response_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response_key, 'tStopRefresh')  # time at next scr refresh
                Response_key.status = FINISHED
        if Response_key.status == STARTED:
            theseKeys = Response_key.getKeys(keyList=['q', 'p'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Response_key.keys = theseKeys.name  # just the last key pressed
                Response_key.rt = theseKeys.rt
                # was this 'correct'?
                if (Response_key.keys == str(Correct)) or (Response_key.keys == Correct):
                    Response_key.corr = 1
                else:
                    Response_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_trial"-------
    for thisComponent in Practice_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    trials.addData('blank500ms.started', blank500ms.tStartRefresh)
    trials.addData('blank500ms.stopped', blank500ms.tStopRefresh)
    trials.addData('perspective.started', perspective.tStartRefresh)
    trials.addData('perspective.stopped', perspective.tStopRefresh)
    trials.addData('blank500.started', blank500.tStartRefresh)
    trials.addData('blank500.stopped', blank500.tStopRefresh)
    trials.addData('numberDots.started', numberDots.tStartRefresh)
    trials.addData('numberDots.stopped', numberDots.tStopRefresh)
    trials.addData('consistent1.started', consistent1.tStartRefresh)
    trials.addData('consistent1.stopped', consistent1.tStopRefresh)
    # check responses
    if Response_key.keys in ['', [], None]:  # No response was made
        Response_key.keys = None
        # was no response the correct answer?!
        if str(Correct).lower() == 'none':
           Response_key.corr = 1;  # correct non-response
        else:
           Response_key.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('Response_key.keys',Response_key.keys)
    trials.addData('Response_key.corr', Response_key.corr)
    if Response_key.keys != None:  # we had a response
        trials.addData('Response_key.rt', Response_key.rt)
    trials.addData('Response_key.started', Response_key.tStart)
    trials.addData('Response_key.stopped', Response_key.tStop)
    if(Response_key.corr == 1):
        total_acc = total_acc + 1
    else:
        total_acc = 0
    if(total_acc >= 5):
        Practice_trial.finished == True
    
    # ------Prepare to start Routine "Blank500ms"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500msComponents = [Blankscreen]
    for thisComponent in Blank500msComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Blank500ms"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500msClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500msClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Blankscreen* updates
        if Blankscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blankscreen.frameNStart = frameN  # exact frame index
            Blankscreen.tStart = t  # local t and not account for scr refresh
            Blankscreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blankscreen, 'tStartRefresh')  # time at next scr refresh
            Blankscreen.setAutoDraw(True)
        if Blankscreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blankscreen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Blankscreen.tStop = t  # not accounting for scr refresh
                Blankscreen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blankscreen, 'tStopRefresh')  # time at next scr refresh
                Blankscreen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500ms"-------
    for thisComponent in Blank500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Blankscreen.started', Blankscreen.tStartRefresh)
    trials.addData('Blankscreen.stopped', Blankscreen.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    if not Response_key.keys:
        msg = "Please respond faster!"
    elif Response_key.corr:
        msg = "Good job!"
    else:
        msg = "Oops! Wrong answer."
    feedbacktext2.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedbacktext2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbacktext2* updates
        if feedbacktext2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            feedbacktext2.frameNStart = frameN  # exact frame index
            feedbacktext2.tStart = t  # local t and not account for scr refresh
            feedbacktext2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbacktext2, 'tStartRefresh')  # time at next scr refresh
            feedbacktext2.setAutoDraw(True)
        if feedbacktext2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbacktext2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedbacktext2.tStop = t  # not accounting for scr refresh
                feedbacktext2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbacktext2, 'tStopRefresh')  # time at next scr refresh
                feedbacktext2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedbacktext2.started', feedbacktext2.tStartRefresh)
    trials.addData('feedbacktext2.stopped', feedbacktext2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
