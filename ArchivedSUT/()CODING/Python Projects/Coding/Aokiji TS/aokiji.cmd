; The CMD file.
;
; Two parts: 1. Command definition and  2. State entry
; (state entry is after the commands def section)
;
; 1. Command definition
; ---------------------
; Note: The commands are CASE-SENSITIVE, and so are the command names.
; The eight directions are:
;   B, DB, D, DF, F, UF, U, UB     (all CAPS)
;   corresponding to back, down-back, down, downforward, etc.
; The six buttons are:
;   a, b, c, x, y, z               (all lower case)
;   In default key config, abc are are the bottom, and xyz are on the
;   top row. For 2 button characters, we recommend you use a and b.
;   For 6 button characters, use abc for kicks and xyz for punches.
;
; Each [Command] section defines a command that you can use for
; state entry, as well as in the CNS file.
; The command section should look like:
;
;   [Command]
;   name = some_name
;   command = the_command
;   time = time (optional)
;   buffer.time = time (optional)
;
; - some_name
;   A name to give that command. You'll use this name to refer to
;   that command in the state entry, as well as the CNS. It is case-
;   sensitive (QCB_a is NOT the same as Qcb_a or QCB_A).
;
; - command
;   list of buttons or directions, separated by commas. Each of these
;   buttons or directions is referred to as a "symbol".
;   Directions and buttons can be preceded by special characters:
;   slash (/) - means the key must be held down
;          egs. command = /D       ;hold the down direction
;               command = /DB, a   ;hold down-back while you press a
;   tilde (~) - to detect key releases
;          egs. command = ~a       ;release the a button
;               command = ~D, F, a ;release down, press fwd, then a
;          If you want to detect "charge moves", you can specify
;          the time the key must be held down for (in game-ticks)
;          egs. command = ~30a     ;hold a for at least 30 ticks, then release
;   dollar ($) - Direction-only: detect as 4-way
;          egs. command = $D       ;will detect if D, DB or DF is held
;               command = $B       ;will detect if B, DB or UB is held
;   plus (+) - Buttons only: simultaneous press
;          egs. command = a+b      ;press a and b at the same time
;               command = x+y+z    ;press x, y and z at the same time
;   greater-than (>) - means there must be no other keys pressed or released
;                      between the previous and the current symbol.
;          egs. command = a, >~a   ;press a and release it without having hit
;                                  ;or released any other keys in between
;   You can combine the symbols:
;     eg. command = ~30$D, a+b     ;hold D, DB or DF for 30 ticks, release,
;                                  ;then press a and b together
;
;   Note: Successive direction symbols are always expanded in a manner similar
;         to this example:
;           command = F, F
;         is expanded when MUGEN reads it, to become equivalent to:
;           command = F, >~F, >F
;
;   It is recommended that for most "motion" commads, eg. quarter-circle-fwd,
;   you start off with a "release direction". This makes the command easier
;   to do.
;
; - time (optional)
;   Time allowed to do the command, given in game-ticks. The default
;   value for this is set in the [Defaults] section below. A typical
;   value is 15.
;
; - buffer.time (optional)
;   Time that the command will be buffered for. If the command is done
;   successfully, then it will be valid for this time. The simplest
;   case is to set this to 1. That means that the command is valid
;   only in the same tick it is performed. With a higher value, such
;   as 3 or 4, you can get a "looser" feel to the command. The result
;   is that combos can become easier to do because you can perform
;   the command early. Attacks just as you regain control (eg. from
;   getting up) also become easier to do. The side effect of this is
;   that the command is continuously asserted, so it will seem as if
;   you had performed the move rapidly in succession during the valid
;   time. To understand this, try setting buffer.time to 30 and hit
;   a fast attack, such as KFM's light punch.
;   The default value for this is set in the [Defaults] section below. 
;   This parameter does not affect hold-only commands (eg. /F). It
;   will be assumed to be 1 for those commands.
;
; If you have two or more commands with the same name, all of them will
; work. You can use it to allow multiple motions for the same move.
;
; Some common commands examples are given below.
;
; [Command] ;Quarter circle forward + x
; name = "QCF_x"
; command = ~D, DF, F, x
;
; [Command] ;Half circle back + a
; name = "HCB_a"
; command = ~F, DF, D, DB, B, a
;
; [Command] ;Two quarter circles forward + y
; name = "2QCF_y"
; command = ~D, DF, F, D, DF, F, y
;
; [Command] ;Tap b rapidly
; name = "5b"
; command = b, b, b, b, b
; time = 30
;
; [Command] ;Charge back, then forward + z
; name = "charge_B_F_z"
; command = ~60$B, F, z
; time = 10
;
; [Command] ;Charge down, then up + c
; name = "charge_D_U_c"
; command = ~60$D, U, c
; time = 10


;-| Button Remapping |-----------------------------------------------------
; This section lets you remap the player's buttons (to easily change the
; button configuration). The format is:
;   old_button = new_button
; If new_button is left blank, the button cannot be pressed.
[Remap]
x = x
y = y
z = z
a = a
b = b
c = c
s = s

;-| Default Values |-------------------------------------------------------

[Defaults]
; Default value for the "time" parameter of a Command. Minimum 1.


; Default value for the "buffer.time" parameter of a Command. Minimum 1,
; maximum 30.



;-| Super Motions |--------------------------------------------------------
;The following two have the same name, but different motion.
;Either one will be detected by a "command = TripleKFPalm" trigger.
;Time is set to 20 (instead of default of 15) to make the move
;easier to do.
;
[command]
name = "icicle"
command = ~D,F,a
time = 20
command.buffer.time = 10

[command]
name = "icicle2"
command = ~D,F,b
time = 20
command.buffer.time = 10

[command]
name = "icicle3"
command = ~D,F,c
time = 20
command.buffer.time = 10

[command]
name = "ava"
command = ~D,F,x
time = 15
command.buffer.time = 8

[command]
name = "peacock"
command = ~D,F,y
time = 15
command.buffer.time = 8

[command]
name = "counterc"
command = ~D,B,c
time = 15
command.buffer.time = 8

[command]
name = "counterb"
command = ~D,B,b
time = 15
command.buffer.time = 8

 [command]
name = "counter"
command = ~D,B,a
time = 15
command.buffer.time = 8

 [command]
name = "pillarC"
command = ~D,D,c
time = 15
command.buffer.time = 8

 [command]
name = "pillarB"
command = ~D,D,b
time = 15
command.buffer.time = 8

[command]
name = "pillarA"
command = ~D,D,a
time = 15
command.buffer.time = 8

 [command]
name = "upper"
command = ~D,F,a
time = 20
command.buffer.time = 8

[command]
name = "upperb"
command = ~D,F,b
time = 15
command.buffer.time = 8

[command]
name = "upperc"
command = ~D,F,c
time = 15
command.buffer.time = 8



;-| Special Motions |------------------------------------------------------


;-| Double Tap |-----------------------------------------------------------
[Command]
name = "FF"     ;Required (do not remove)
command = F, F
time = 10

[Command]
name = "BB"     ;Required (do not remove)
command = B, B
time = 10

;-| 2/3 Button Combination |-----------------------------------------------
[Command]
name = "recovery";Required (do not remove)
command = x+y
time = 1

;-| Dir + Button |---------------------------------------------------------
[Command]
name = "down_a"
command = /$D,a
time = 1

[Command]
name = "down_b"
command = /$D,b
time = 1

;-| Single Button |---------------------------------------------------------
[Command]
name = "a"
command = a
time = 1

[Command]
name = "b"
command = b
time = 1

[Command]
name = "c"
command = c
time = 1

[Command]
name = "x"
command = x
time = 1

[Command]
name = "y"
command = y
time = 1

[Command]
name = "z"
command = z
time = 1

[Command]
name = "start"
command = s
time = 1

;-| Hold Dir |--------------------------------------------------------------
[Command]
name = "holdfwd";Required (do not remove)
command = /$F
time = 1

[Command]
name = "holdback";Required (do not remove)
command = /$B
time = 1

[Command]
name = "holdup" ;Required (do not remove)
command = /$U
time = 1

[Command]
name = "holddown";Required (do not remove)
command = /$D
time = 1

[command]
name = "hold_s"
command = /s
time = 15

;---------------------------------------------------------------------------
[Command]
name = "ReF"
command = $F
time = 1
buffer.time=6

[Command]
name = "ReB"
command = $B
time = 1
buffer.time=6

[Command]
name = "ReU"
command = $U
time = 1
buffer.time=6
;---------------------------------------------------------------------------
; 2. State entry
; --------------
; This is where you define what commands bring you to what states.
;
; Each state entry block looks like:
;   [State -1, Label]           ;Change Label to any name you want to use to
;                               ;identify the state with.
;   type = ChangeState          ;Don't change this
;   value = new_state_number
;   trigger1 = command = command_name
;   . . .  (any additional triggers)
;
; - new_state_number is the number of the state to change to
; - command_name is the name of the command (from the section above)
; - Useful triggers to know:
;   - statetype
;       S, C or A : current state-type of player (stand, crouch, air)
;   - ctrl
;       0 or 1 : 1 if player has control. Unless "interrupting" another
;                move, you'll want ctrl = 1
;   - stateno
;       number of state player is in - useful for "move interrupts"
;   - movecontact
;       0 or 1 : 1 if player's last attack touched the opponent
;                useful for "move interrupts"
;
; Note: The order of state entry is important.
;   State entry with a certain command must come before another state
;   entry with a command that is the subset of the first.
;   For example, command "fwd_a" must be listed before "a", and
;   "fwd_ab" should come before both of the others.
;
; For reference on triggers, see CNS documentation.
;
; Just for your information (skip if you're not interested):
; This part is an extension of the CNS. "State -1" is a special state
; that is executed once every game-tick, regardless of what other state
; you are in.


; Don't remove the following line. It's required by the CMD standard.
[Statedef -1]

;Icicle
[State -1, Icicle]
type = ChangeState
value = 660
triggerall = command = "icicle"
trigger1 = (statetype = A) && ctrl
trigger2 = movehit
trigger2 = stateno = 600
trigger2 = time > 6
trigger3 = movehit
trigger3 = stateno = 610
trigger3 = time > 6

;Icicle
[State -1, Icicle 2]
type = ChangeState
value = 670
triggerall = command = "icicle2"
trigger1 = (statetype = A) && ctrl
trigger2 = movehit
trigger2 = stateno = 600
trigger2 = time > 6
trigger3 = movehit
trigger3 = stateno = 610
trigger3 = time > 6

;Icicle
[State -1, Icicle 2]
type = ChangeState
value = 670
triggerall = command = "icicle3"
triggerall = power <= 1000
trigger1 = (statetype = A) && ctrl
trigger2 = movehit
trigger2 = stateno = 600
trigger2 = time > 6
trigger3 = movehit
trigger3 = stateno = 610
trigger3 = time > 6

;Icicle 3
[State -1, Icicle 3]
type = ChangeState
value = 680
triggerall = command = "icicle3"
triggerall = power >= 1000
trigger1 = (statetype = A) && ctrl
trigger2 = movehit
trigger2 = stateno = 600
trigger2 = time > 6
trigger3 = movehit
trigger3 = stateno = 610
trigger3 = time > 6

;Avalanche
[State -1, Avalanche]
type = ChangeState
value = 540
triggerall = command = "ava"
triggerall = statetype != A
triggerall = power >= 1500
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;Pheasant
[State -1, Pheasant]
type = ChangeState
value = 530
triggerall = command = "peacock"
triggerall = statetype != A
triggerall = power >= 2000
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;Counter Special
[State -1, Counter Special]
type = ChangeState
value = 370
triggerall = command = "counterc"
triggerall = power >= 1000
triggerall = statetype != A
trigger1 = (statetype = s) && ctrl

;Counter C
[State -1, Counter C]
type = ChangeState
value = 350
triggerall = command = "counterc"
triggerall = power < 1000
trigger1 = (statetype = s) && ctrl

;Counter B
[State -1, Counter B]
type = ChangeState
value = 350
triggerall = command = "counterb"
trigger1 = (statetype = s) && ctrl

;Counter A
[State -1, Counter A]
type = ChangeState
value = 340
triggerall = command = "counter"
triggerall = statetype != A
trigger1 = (statetype = s) && ctrl

;Ice Pillar Special
[State -1, Ice Pillar Special]
type = ChangeState
value = 360
triggerall = command = "pillarC"
triggerall = power >= 1000
triggerall = statetype != A
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;Ice Pillar B
[State -1, Ice Pillar B]
type = ChangeState
value = 330
triggerall = command = "pillarB"
triggerall = statetype != A
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;Ice Pillar
[State -1, Ice Pillar]
type = ChangeState
value = 320
triggerall = command = "pillarA"
triggerall = statetype != A
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;Ice Upper Special
[State -1, Ice Upper Special]
type = ChangeState
value = 520
triggerall = command = "upperc"
triggerall = power >= 1000
triggerall = statetype != A
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;Ice Upper C
[State -1, Ice Upper C]
type = ChangeState
value = 310
triggerall = command = "upperc"
triggerall = power < 1000
triggerall = statetype != A
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;Ice Upper Double
[State -1, Ice Upper Double]
type = ChangeState
value = 310
triggerall = command = "upperb"
triggerall = statetype != A
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;Ice Upper
[State -1, Ice Upper]
type = ChangeState
value = 300
triggerall = command = "upper"
triggerall = statetype != A
trigger1 = movecontact
trigger1 = stateno = 200
trigger1 = time > 7
trigger2 = movecontact
trigger2 = stateno = 210
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 230
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 240
trigger4 = time > 7
trigger5 = statetype = S
trigger5 = ctrl

;===========================================================================
;Run Fwd
[State -1, Run Fwd]
type = ChangeState
value = 100
trigger1 = command = "FF"
trigger1 = statetype = S
trigger1 = ctrl

;---------------------------------------------------------------------------
;Run Back
[State -1, Run Back]
type = ChangeState
value = 105
trigger1 = command = "BB"
trigger1 = statetype = S
trigger1 = ctrl

;---------------------------------------------------------------------------
;Down Z
[State -1, Down Z]
type = ChangeState
value = 198
triggerall = command = "z"
triggerall = power >= 250
;triggerall = command != "holddown"
trigger1 = statetype = C
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 200
trigger2 = time > 7
trigger3 = movehit
trigger3 = stateno = 210
trigger3 = time > 7

;---------------------------------------------------------------------------
;Z
[State -1, Z]
type = ChangeState
value = 199
triggerall = command = "z"
triggerall = command != "holddown"
triggerall = power >= 250
trigger1 = statetype = S
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 200
trigger2 = time > 7
trigger3 = movehit
trigger3 = stateno = 210
trigger3 = time > 7


;---------------------------------------------------------------------------
;A
[State -1, A]
type = ChangeState
value = 200
triggerall = command = "a"
triggerall = command != "holddown"
triggerall = stateno != [100,101]
trigger1 = statetype = S
trigger1 = ctrl
trigger2 = stateno = 200
trigger2 = time > 7
trigger3 = stateno = 210
trigger3 = time > 7
trigger4 = stateno = 205
trigger4 = time > 7
;trigger3 = fvar(20)=1

;---------------------------------------------------------------------------
;Running Slice
[State -1, Running Slice]
type = ChangeState
value = 205
triggerall = stateno = [100,101]
trigger1 = command="a"
trigger2 = command="b"
trigger3 = command="c"

;---------------------------------------------------------------------------
;B
[State -1, B]
type = ChangeState
value = 210
triggerall = command = "b"
triggerall = command != "holddown"
triggerall = stateno != [100,101]
trigger1 = statetype = S
trigger1 = ctrl
trigger2 = movecontact
trigger2 = stateno = 200
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 210
trigger3 = time > 7
trigger4 = stateno = 205
trigger4 = time > 7

;---------------------------------------------------------------------------
;C
[State -1, C]
type = ChangeState
value = 220
triggerall = command = "c"
triggerall = command != "holddown"
triggerall = stateno != [100,101]
trigger1 = statetype = S
trigger1 = ctrl
trigger2 = movecontact
trigger2 = stateno = 200
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 210
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 230
trigger4 = time > 7
trigger5 = movecontact
trigger5 = stateno = 240
trigger5 = time > 7

;---------------------------------------------------------------------------
;X
[State -1, X]
type = ChangeState
value = 260
triggerall = command = "x"
triggerall = command != "holddown"
trigger1 = statetype = S
trigger1 = ctrl
trigger2 = movecontact
trigger2 = stateno = 200
trigger2 = time > 7
trigger3 = movecontact
trigger3 = stateno = 210
trigger3 = time > 7
trigger4 = movecontact
trigger4 = stateno = 230
trigger4 = time > 7
trigger5 = movecontact
trigger5 = stateno = 240
trigger5 = time > 7

;---------------------------------------------------------------------------
;X 2nd Hit
[State -1, X 2nd Hit]
type = ChangeState
value = 270
triggerall = command = "x"
triggerall = command != "holddown"
trigger1 = statetype = S
;trigger1 = ctrl
trigger1 = movecontact
trigger1 = stateno = 260
trigger1 = time > 23
;---------------------------------------------------------------------------
;Crouch A
[State -1, Crouch A]
type = ChangeState
value = 230
triggerall = command = "a"
triggerall = command = "holddown"
trigger1 = statetype = C
trigger1 = ctrl
trigger2 = stateno = 200
trigger2 = time > 5
trigger3 = stateno = 210
trigger3 = time > 5

;---------------------------------------------------------------------------
;Crouch B
[State -1, Crouch B]
type = ChangeState
value = 240
triggerall = command = "b"
triggerall = command = "holddown"
triggerall = command != "holdfwd"
trigger1 = statetype = C
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 200
trigger2 = time > 5
trigger3 = movehit
trigger3 = stateno = 210
trigger3 = time > 5
trigger4 = movehit
;trigger4 = prevstateno != 240
trigger4 = stateno = 230
trigger4 = time > 11

;---------------------------------------------------------------------------
;Crouch C
[State -1, Crouch C]
type = ChangeState
value = 250
triggerall = command = "c"
triggerall = command = "holddown"
triggerall = command != "holdfwd"
trigger1 = statetype = C
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 200
trigger2 = time > 5
trigger3 = movehit
trigger3 = stateno = 210
trigger3 = time > 5
trigger4 = movehit
trigger4 = stateno = 230
trigger4 = time > 7
trigger5 = movehit
trigger5 = stateno = 240
trigger5 = time > 7

;---------------------------------------------------------------------------
;Crouch x
[State -1, Crouch X]
type = ChangeState
value = 290
triggerall = command = "x"
triggerall = command = "holddown"
triggerall = command != "holdfwd"
trigger1 = statetype = C
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 200
trigger2 = time > 5
trigger3 = movehit
trigger3 = stateno = 210
trigger3 = time > 5
trigger4 = movehit
trigger4 = stateno = 230
trigger4 = time > 7
trigger5 = movehit
trigger5 = stateno = 240
trigger5 = time > 7
trigger6 = movehit
trigger6 = stateno = 220
trigger6 = time > 7

;---------------------------------------------------------------------------
;Crouch Y
[State -1, Crouch Y]
type = ChangeState
value = 280
triggerall = command = "y"
triggerall = command = "holddown"
triggerall = command != "holdfwd"
trigger1 = statetype = C
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 200
trigger2 = time > 5
trigger3 = movehit
trigger3 = stateno = 210
trigger3 = time > 5
trigger4 = movehit
trigger4 = stateno = 230
trigger4 = time > 7
trigger5 = movehit
trigger5 = stateno = 240
trigger5 = time > 7

;---------------------------------------------------------------------------
;Jump A
[State -1, Jump A]
type = ChangeState
value = 600
triggerall = command = "a"
trigger1 = statetype = A
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 610
trigger2 = time > 5
;---------------------------------------------------------------------------
;Jump B
[State -1, Jump B]
type = ChangeState
value = 610
triggerall = command = "b"
triggerall = command != "holddown"
trigger1 = statetype = A
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 600
trigger2 = time > 5
;trigger3 = movehit
;trigger3 = stateno = 250
;trigger3 = time > 9

;---------------------------------------------------------------------------
;Jump Down A
[State -1, Jump Y]
type = ChangeState
value = 640
triggerall = command = "y"
;triggerall = command = "holddown"
trigger1 = statetype = A
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 600
trigger2 = time > 6
trigger3 = movehit
trigger3 = stateno = 610
trigger3 = time > 6

;---------------------------------------------------------------------------
;Jump C
[State -1, Jump C]
type = ChangeState
value = 620
triggerall = command = "c"
triggerall = command != "holddown"
trigger1 = statetype = A
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 600
trigger2 = time > 5
trigger3 = movehit
trigger3 = stateno = 610
trigger3 = time > 5

;---------------------------------------------------------------------------
;Jump Down C
[State -1, Jump Z]
type = ChangeState
value = 650
triggerall = command = "z"
;triggerall = command = "holddown"
trigger1 = statetype = A
trigger1 = ctrl
trigger2 = movehit
trigger2 = stateno = 600
trigger2 = time > 6
trigger3 = movehit
trigger3 = stateno = 610
trigger3 = time > 6

;---------------------------------------------------------------------------
[State -1, Charge]
type = ChangeState
value = 910
triggerall = power != 3000
triggerall = command = "hold_s"
triggerall = statetype = S
trigger1 = ctrl

