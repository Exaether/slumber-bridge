# Full version

- name
  a simple line, with the character name

- animtext
  place or temporal context ("Londinium, victoria, 1:12 PM")

- animtextclean
  clear the animtext

- subtitle
  narration text
  can be used bare to clear the subtitle state

- sticker
  subtitle, but persistent until cleared
  bare with only id to clear

- stickerclear
  remove all stickers

- dialog
  beginning of a dialog

- blocker
  full screen overlay, have some params such as color and fadetime

- charslot
  standard way of displaying sprites on the screen
  `slot` param selects the position (l, m, r) and other params put a sprite on it, change it, or apply an action (move, scale, etc)
  can be used bare to clear the slots

- character
  make a sprite appear, not sure if it's simply an older method or not.
  can be used bare to clear sprites, not sure if it also clear charslots

- cgitem
  show a cg element, like kal's coat falling into the ground

- hidecgitem
  hide a cg item

- showitem
  show an item

- hideitem
  hide it

- focusout
  push an element out of focus, can use different methods (dim, etc), "type" param define what it affects

- focusparam
  determine what effect is used, mostly not used

- playmusic / playsound
  start a bgm/sfx
- musicvolume / soundvolume
  adjust the bgm/sfx volume
- stopmusic / stopsound
  stop the bgm/sfx

- curtain
  fill a part of the screen

- effect
  vfx

- cameraeffect

- camerashake

- avgdisplay
  avg control

- theater
  set theater mode

- video
  play a video

- delay

- background
  set the background, bare to clear the bg

- bgeffect
  apply an effect on the bg, bare to clear the effect

- gridbg
  load a grid of bgs. bare to clear
- largebg
  load multiple bgs in a strip (for panoramas), bare to clear
- verticalbg
  load multiple bgs in a vertical strip, bare to clear

- image
  fullscreen image, bare to clear
- imagerotate
  rotate the current image
- imgeffect
  effect (screen distortion or gate open in babel) bare to clear

- characteraction
  animate a sprite

- imagetween / backgroundtween / largebgtween
  animate a property

- interlude
  way to apply a mask or an effect ig

- charactercutin
  phone transmission (char in a box)

- timersticker
  displays a timer
- timerclear

- spellsticker
  display an effect overlay (only on ch 17, pretty new)
- spellstickerclear

- decision
  doc dialog options
  options separated by ;
- predicate
  skip node for options
  references say if the following text should be displayed

# Stripped down version

- name
- animtext
- animtextclean
- subtitle
- sticker
- stickerclear
- dialog
- blocker
- charslot
- character
- cgitem
- hidecgitem
- showitem
- hideitem
- playmusic
- stopmusic
- playsound
- stopsound
- video
- background
- bgeffect
- gridbg
- largebg
- verticalbg
- image
- charactercutin
- decision
- predicate
