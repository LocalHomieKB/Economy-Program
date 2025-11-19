;===============================================================================
;-------------------------------Comandos----------------------------------------
;===============================================================================
[Remap]
x = x
y = y
z = z
a = a
b = b
c = c
s = s

;----------------------------SUPERS-------------------------;






[Command]
name = "Shin Sekai Strike"
command = ~x
time = 30
[Command]
name = "Shin Sekai Strike"
command = ~x
time = 30

[Command]
name = "Haoshoku Haki"
command = ~y
time = 30
[Command]
name = "Haoshoku Haki"
command = ~y
time = 30


[Command]
name = "Heaven Splitter"
command = ~z
time = 30
[Command]
name = "Heaven Splitter"
command = ~z
time = 30


;----------------------------SPECIALS-------------------------;



[Command]
name = "ShotGun"
command = ~DF,c
time = 20
[Command]
name = "ShotGun"
command = ~DF,c
time = 20


[Command]
name = "Rush Double Kick"
command = ~DB,c
time = 30
[Command]
name = "Rush Double Kick"
command = ~DB,c
time = 30


[Command]
name = "Pirate Catch"
command = ~DF,a
time = 20
[Command]
name = "Pirate Catch"
command = ~DF,a
time = 20


[Command]
name = "Tatami Gaeshi"
command = ~DB,a
time = 20
[Command]
name = "Tatami Gaeshi"
command = ~DB,a
time = 20


[Command]
name = "Revenge Counter"
command = ~D,s
time = 20
[Command]
name = "Revenge Counter"
command = ~D,s
time = 20


[Command]
name = "Chaoz Slash"
command = ~DF,b
time = 20
[Command]
name = "Chaoz Slash"
command = ~DF,b
time = 20

[Command]
name = "Red Hair Assault"
command = ~DB,b
time = 20
[Command]
name = "Red Hair Assault"
command = ~DB,b
time = 20


[Command]
name = "Haki POW UP"
command = ~D,D,c
time = 25

;-| Default Values |-------------------------------------------------------
[Defaults]

command.time = 30
[command]
name = "Super Jump"
command = ~D,U
time = 10

command.buffer.time = 1
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
name = "recovery" ;Required (do not remove)
command = x+y
time = 1

[Command]
name = "recovery"
command = y+z
time = 1

[Command]
name = "recovery"
command = x+z
time = 1

[Command]
name = "recovery"
command = a+b
time = 1

[Command]
name = "recovery"
command = b+c
time = 1

[Command]
name = "recovery"
command = a+c
time = 1
;-| Dir + Button |---------------------------------------------------------
[Command]
name = "back_x"
command = /$B,x
time = 1

[Command]
name = "back_y"
command = /$B,y
time = 1

[Command]
name = "back_z"
command = /$B,z
time = 1

[Command]
name = "down_x"
command = /$D,x
time = 1

[Command]
name = "down_y"
command = /$D,y
time = 1

[Command]
name = "down_z"
command = /$D,z
time = 1

[Command]
name = "fwd_x"
command = /$F,x
time = 1

[Command]
name = "fwd_y"
command = /$F,y
time = 1

[Command]
name = "fwd_z"
command = /$F,z
time = 1

[Command]
name = "up_x"
command = /$U,x
time = 1

[Command]
name = "up_y"
command = /$U,y
time = 1

[Command]
name = "up_z"
command = /$U,z
time = 1

[Command]
name = "back_a"
command = /$B,a
time = 1

[Command]
name = "back_b"
command = /$B,b
time = 1

[Command]
name = "back_c"
command = /$B,c
time = 1

[Command]
name = "down_a"
command = /$D,a
time = 1

[Command]
name = "down_b"
command = /$D,b
time = 1

[Command]
name = "down_c"
command = /$D,c
time = 1

[Command]
name = "fwd_a"
command = /$F,a
time = 1

[Command]
name = "fwd_b"
command = /$F,b
time = 1

[Command]
name = "fwd_c"
command = /$F,c
time = 1

[Command]
name = "up_a"
command = /$U,a
time = 1

[Command]
name = "up_b"
command = /$U,b
time = 1

[Command]
name = "up_c"
command = /$U,c
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
name = "s"
command = s
time = 1
;-| Single Dir |------------------------------------------------------------
[Command]
name = "fwd" ;Required (do not remove)
command = $F
time = 1

[Command]
name = "downfwd"
command = $DF
time = 1

[Command]
name = "down" ;Required (do not remove)
command = $D
time = 1

[Command]
name = "downback"
command = $DB
time = 1

[Command]
name = "back" ;Required (do not remove)
command = $B
time = 1

[Command]
name = "upback"
command = $UB
time = 1

[Command]
name = "up" ;Required (do not remove)
command = $U
time = 1

[Command]
name = "upfwd"
command = $UF
time = 1
;-| Hold Button |--------------------------------------------------------------
[Command]
name = "hold_x"
command = /x
time = 1

[Command]
name = "hold_y"
command = /y
time = 1

[Command]
name = "hold_z"
command = /z
time = 1

[Command]
name = "hold_a"
command = /a
time = 1

[Command]
name = "hold_b"
command = /b
time = 1

[Command]
name = "hold_c"
command = /c
time = 1

[Command]
name = "hold_s"
command = /s
time = 1
;-| Hold Dir |--------------------------------------------------------------
[Command]
name = "holdfwd" ;Required (do not remove)
command = /$F
time = 1

[Command]
name = "holddownfwd"
command = /$DF
time = 1

[Command]
name = "holddown" ;Required (do not remove)
command = /$D
time = 1

[Command]
name = "holddownback"
command = /$DB
time = 1

[Command]
name = "holdback" ;Required (do not remove)
command = /$B
time = 1

[Command]
name = "holdupback"
command = /$UB
time = 1

[Command]
name = "holdup" ;Required (do not remove)
command = /$U
time = 1

[Command]
name = "holdupfwd"
command = /$UF
time = 1
;---------- Comandos de la Inteligencia Artificial-----------------
; Comandos activadores
;[Command]
;name = "AI Prueba"
;command = y+z ; con el botón A+B activamos la AI
;time = 1

;[Command]
;name = "AI desactivado"
;command = x+y ; Con el boton B+C desactivamos la AI
;time = 1

;---------- comandos para que la PC active la IA -------------------------
[command]
name = "AI1"
command = b,b,b,b,b,b,b,b,b,b,b
time = 1

[command]
name = "AI2"
command = b,c,b,c,b,c,b,c,b,c,b,c
time = 1

[command]
name = "AI3"
command = b,c,b,c,b,c,b,c,b,c,b
time = 1

[command]
name = "AI4"
command = a,b,a,b,a,b,a,b,a,b,a
time = 1

[command]
name = "AI5"
command = b,a,b,a,b,a,b,a,b,a,b
time = 1

[command]
name = "AI6"
command = b,b,b,b,z,b,z,b,z,z,z
time = 1

[command]
name = "AI7"
command = b,x,b,b,x,b,b,b,b,b,x
time = 1

[command]
name = "AI8"
command = b,y,b,b,b,y,b,b,b,b,y
time = 1

[command]
name = "AI9"
command = b,b,b,b,s,z,y,x,c,b,a
time = 1

[command]
name = "AI10"
command = z,b,x,y,b,b,c,b,b,b,a
time = 1

[command]
name = "AI11"
command = b,x,b,b,x,b,b,b,b,b,z
time = 1

[command]
name = "AI12"
command = b,y,b,s,b,y,b,b,b,b,y
time = 1

[command]
name = "AI13"
command = b,b,b,z,s,z,y,x,c,b,a
time = 1

[command]
name = "AI14"
command = z,b,x,y,b,b,c,b,b,c,a
time = 1
;---------------------------------------------------------------------------
[Statedef -1]
;===========================================================================
;---------------------------Basicos-----------------------------------------
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
; Correr Adelante Haki
[State -1, Correr Adelante]
type = ChangeState
triggerall = var(14) = 1
value = 107
trigger1 = command = "FF"
trigger1 = statetype = S
trigger1 = ctrl
;---------------------------------------------------------------------------
; Correr Atras  Haki
[State -1, Correr Atras]
type = ChangeState
triggerall = var(14) = 1
value = 108
trigger1 = command = "BB"
trigger1 = statetype = S
trigger1 = ctrl
;---------------------------------------------------------------------------

; Correr Adelante
[State -1, Correr Adelante]
type = ChangeState
triggerall = var(14) = 0
value = 100
trigger1 = command = "FF"
trigger1 = statetype = S
trigger1 = ctrl
;---------------------------------------------------------------------------
; Correr Atras
[State -1, Correr Atras]
type = ChangeState
triggerall = var(14) = 0
value = 105
trigger1 = command = "BB"
trigger1 = statetype = S
trigger1 = ctrl
;---------------------------------------------------------------------------
;Super Jump
[State -1, Super Jump]
type            = ChangeState
value      = 60
triggerall      = command = "Super Jump"
trigger1        = (statetype = S) && (ctrl)

;===========================================================================
;--------------------------------Ataques Specials-----------------------------
;---------------------------------------------------------------------------



;Shin Sekai Strike
[State -1, Shin Sekai Strike]
type = ChangeState
value = 3300
triggerall = Power >= 2000
triggerall = command = "Shin Sekai Strike"
trigger1 = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)
trigger10 = (stateno = 1110) && (Movecontact)
trigger11 = (stateno = 1121) && (Movecontact)
trigger12 = (stateno = 1310) && (Movecontact)
trigger13 = (stateno = 1400) && (time > 25)
trigger14 = (stateno = 1700) && (time > 34)


;Haoshoku Haki
[State -1, Haoshoku Haki]
type = ChangeState
value = 3200
triggerall = Power >= 1000
triggerall = numhelper(1010) = 0
triggerall = numhelper(1020) = 0
triggerall = command = "Haoshoku Haki"
trigger1 = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)
trigger10 = (stateno = 1110) && (Movecontact)
trigger11 = (stateno = 1121) && (Movecontact)
trigger12 = (stateno = 1310) && (Movecontact)
trigger13 = (stateno = 1400) && (time > 25)
trigger14 = (stateno = 1700) && (time > 34)


;Heaven Splitter Air
[State -1, Heaven Splitter Air]
type = ChangeState
value = 3100
triggerall = Power >= 1000
triggerall = command = "Heaven Splitter"
trigger1 = statetype = A
trigger1 = ctrl
trigger2 = (stateno = 600) && (Movecontact)
trigger3 = (stateno = 610) && (Movecontact)
trigger4 = (stateno = 620) && (Movecontact)
trigger5 = (stateno = 625) && (Movecontact)
trigger6 = (stateno = 630) && (Movecontact)
trigger7 = (stateno = 635) && (Movecontact)
trigger8 = (stateno = 1630) && (Movecontact)



;Heaven Splitter
[State -1, Heaven Splitter]
type = ChangeState
value = 3000
triggerall = Power >= 1000
triggerall = command = "Heaven Splitter"
trigger1 = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)
trigger10 = (stateno = 1110) && (Movecontact)
trigger11 = (stateno = 1121) && (Movecontact)
trigger12 = (stateno = 1310) && (Movecontact)
trigger13 = (stateno = 1400) && (time > 25)
trigger14 = (stateno = 1700) && (time > 34)

;===========================================================================
;--------------------------------Ataques Specials-----------------------------
;---------------------------------------------------------------------------


;---------------------------------------------------------------------------
;Haki POW UP
[State -1, Haki POW UP]
type = ChangeState
value = 1800
triggerall = var(14) = 0
triggerall = numhelper(1840) = 0
triggerall = command = "Haki POW UP"
triggerall = statetype != A
trigger1 = ctrl

;---------------------------------------------------------------------------
;ShotGun
[State -1, ShotGun]
type = ChangeState
value = 1700
triggerall = command = "ShotGun"
triggerall = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)
trigger10 = (stateno = 1110) && (Movecontact)
trigger11 = (stateno = 1121) && (Movecontact)
trigger12 = (stateno = 1310) && (Movecontact)
trigger13 = (stateno = 1400) && (time > 25)


;---------------------------------------------------------------------------
;Rush Double Kick
[State -1, Rush Double Kick]
type = ChangeState
value = 1600
triggerall = command = "Rush Double Kick"
triggerall = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)
trigger10 = (stateno = 1110) && (Movecontact)
trigger11 = (stateno = 1121) && (Movecontact)
trigger12 = (stateno = 1310) && (Movecontact)
trigger13 = (stateno = 1400) && (time > 25)
trigger14 = (stateno = 1700) && (time > 34)

;---------------------------------------------------------------------------
; Pirate Catch
[State -1, Pirate Catch]
type = ChangeState
value = 1500
triggerall = command = "Pirate Catch"
triggerall = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)
trigger10 = (stateno = 1110) && (Movecontact)
trigger11 = (stateno = 1121) && (Movecontact)
trigger12 = (stateno = 1310) && (Movecontact)
trigger13 = (stateno = 1400) && (time > 25)
trigger14 = (stateno = 1700) && (time > 34)

;---------------------------------------------------------------------------
; Tatami Gaeshi
[State -1, Tatami Gaeshi]
type = ChangeState
value = 1400
triggerall = command = "Tatami Gaeshi"
triggerall = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)
trigger10 = (stateno = 1110) && (Movecontact)
trigger11 = (stateno = 1121) && (Movecontact)


;---------------------------------------------------------------------------
; Revenge Counter
[State -1, Revenge Counter]
type = ChangeState
value = 1300
triggerall = command = "Revenge Counter"
triggerall = statetype != A
trigger1 = ctrl


;---------------------------------------------------------------------------
; Chaoz Slash
[State -1, Chaoz Slash]
type = ChangeState
value = 1200
triggerall = command = "Chaoz Slash"
triggerall = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)
trigger10 = (stateno = 1110) && (Movecontact)
trigger11 = (stateno = 1121) && (Movecontact)
trigger12 = (stateno = 1310) && (Movecontact)
trigger13 = (stateno = 1400) && (time > 25)
trigger14 = (stateno = 1700) && (time > 34)


;---------------------------------------------------------------------------
; Red Hair Assault
[State -1, Red Hair Assault]
type = ChangeState
value = 1100
triggerall = command = "Red Hair Assault"
triggerall = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
trigger6 = (stateno = 220) && (Movecontact)
trigger7 = (stateno = 225) && (Movecontact)
trigger8 = (stateno = 230) && (Movecontact)
trigger9 = (stateno = 235) && (Movecontact)






;===========================================================================
;--------------------------------Ataques Especiales-------------------------
;---------------------------------------------------------------------------

;===========================================================================
;--------------------------------Ataques Normales---------------------------
;---------------------------------------------------------------------------
; Burla
[State -1, Taunt]
type = ChangeState
value = 195
triggerall = command = "hold_s"
triggerall = power < 3000
trigger1 = statetype != A
trigger1 = ctrl

;---------------------------------------------------------------------------
; Espadazos Run
[State -1, Espadazos]
type = ChangeState
value = 300
triggerall = command = "a"
triggerall = stateno = 100 ||  stateno = 107
trigger1 = statetype != A
trigger1 = ctrl

;---------------------------------------------------------------------------
; Patada Run
[State -1, Patada]
type = ChangeState
value = 310
triggerall = command = "b"
triggerall = stateno = 100 ||  stateno = 107
trigger1 = statetype != A
trigger1 = ctrl

;---------------------------------------------------------------------------
; Espadazos
[State -1, Espadazos]
type = ChangeState
value = 200
triggerall = command = "a"
trigger1 = statetype != A
trigger1 = ctrl

;---------------------------------------------------------------------------
; Kick Up
[State -1, Kick Up]
type = ChangeState
value = 211
triggerall = command = "b"
triggerall = command = "holddown"
trigger1 = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
;---------------------------------------------------------------------------
; Patada
[State -1, Patada]
type = ChangeState
value = 210
triggerall = command = "b"
trigger1 = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)

;---------------------------------------------------------------------------
; Haushoku Haki - Anti Combos
[State -1, Haushoku Haki - Anti Combos]
type = ChangeState
value = ifelse(var(14)=1,235,230)
triggerall = command = "c"
triggerall = numhelper(1020) = 0
triggerall = numhelper(1010) = 0
triggerall = power >= 1000
triggerall = stateno = [5000,5019]
trigger1 = movetype = H
trigger1 = ctrl = 0



;---------------------------------------------------------------------------
; Haushoku Haki
[State -1, Haushoku Haki]
type = ChangeState
value = ifelse(var(14)=1,225,220)
triggerall = command = "c"
triggerall = numhelper(1010) = 0
triggerall = numhelper(1020) = 0
trigger1 = statetype != A
trigger1 = ctrl
trigger2 = (stateno = 200) && (Movecontact)
trigger3 = (stateno = 201) && (Movecontact)
trigger4 = (stateno = 210) && (Movecontact)
trigger5 = (stateno = 211) && (Movecontact)
;---------------------------------------------------------------------------
; Espadazo Aire
[State -1, Espadazo Aire]
type = ChangeState
value = 600
triggerall = command = "a"
trigger1 = statetype = A
trigger1 = ctrl

;---------------------------------------------------------------------------
; Patada Aire
[State -1, Patada Aire]
type = ChangeState
value = 610
triggerall = command = "b"
trigger1 = statetype = A
trigger1 = ctrl
trigger2 = (stateno = 600) && (Movecontact)


;---------------------------------------------------------------------------
; Haushoku Haki Aire - Anti Combos
[State -1, Haushoku Haki - Anti Combos]
type = ChangeState
value = ifelse(var(14)=1,635,630)
triggerall = command = "c"
triggerall = numhelper(1020) = 0
triggerall = numhelper(1010) = 0
triggerall = power >= 1000
triggerall = stateno = [5020,5080]
trigger1 = movetype = H
trigger1 = ctrl = 0


;---------------------------------------------------------------------------
; Haushoku Haki  Aire
[State -1, Ataque Aire]
type = ChangeState
value = ifelse(var(14)=1,625,620)
triggerall = command = "c"
triggerall = numhelper(1010) = 0
triggerall = numhelper(1020) = 0
trigger1 = statetype = A
trigger1 = ctrl
trigger2 = (stateno = 600) && (Movecontact)
trigger3 = (stateno = 610) && (Movecontact)


;-------------------------------------------------------------------------------
; Activar IA
;-------------------------------------------------------------------------------
[State -2, Activar IA]
type = VarSet
trigger1 = (command = "AI1") ||(Command = "AI2") || (Command = "AI3") || (Command = "AI4") || (Command = "AI5")
trigger2 = (Command = "AI6") || (Command = "AI7") || (Command = "AI8") || (Command = "AI9") || (Command = "AI10")
trigger4 = (Command = "AI11") || (Command = "AI12") || (Command = "AI13") || (Command = "AI14")
var(9) = 1
