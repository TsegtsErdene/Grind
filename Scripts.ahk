#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
dir    := "C:\Users\Tsegts-ErdeneGantulg\Desktop\sites\Grind"
script  = %dir%\test.py
buy = buy


; !f::
; InputBox, UserInput, How many, Please enter a number, , 200, 150
; if !ErrorLevel
;     Run, %ComSpec% /k python %dir%\gold.py buy %UserInput% && exit
; return

!g::
InputBox, UserInput, How many, Please enter a number, , 200, 150
if !ErrorLevel
    Run, %ComSpec% /k python %dir%\gold.py buy %UserInput% goldinone && exit
return


; !b::
; InputBox, UserInput, How many, Please enter a number, , 200, 150
; if !ErrorLevel
;     Run, %ComSpec% /k python %dir%\gold.py sell %UserInput% && exit
; return


!v::
InputBox, UserInput, How many, Please enter a number, , 200, 150
if !ErrorLevel
    Run, %ComSpec% /k python %dir%\gold.py sell %UserInput% goldinone && exit
return


!r::
Run, %ComSpec% /k python %dir%\forceclose.py && exit
return

!t::
InputBox, UserInput, How many, Please enter a number, , 200, 150
if !ErrorLevel
    Run, %ComSpec% /k python %dir%\forceclose.py %UserInput% && exit
return


