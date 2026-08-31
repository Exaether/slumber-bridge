- name

- animtext
  place or temporal context ("Londinium, victoria, 1:12 PM")

- animtextclean
  clear the animtext, there is one more than animtext, ig it can stay...

- subtitle
  narration text
  can be used bare to clear the subtitle state

- dialog
  beginning of a dialog

- blocker
  full screen overlay, have some params such as color and fadetime

- charslot
  fill a slot (l, m, r) with a sprite, or change the sprite, or apply an action (focus change, scale, etc)
  can be used bare to clear the slots

- character
  make a sprite appear, have some useful params
  can be used bare, apparently also to clear the slots, maybe only clear "character" slots and not "charslots"

- cgitem
  show a cg element, like kal's coat falling into the ground

- hidecgitem
  hide a cg item

- showitem
  show an item

- hideitem
  hide it

- sticker
  subtitle, but persistent until cleared
  bare with only id to clear

- stickerclear
  remove all stickers

- focusout
  push an element out of focus (probably dim or smtg), "type" param define what it affects

- focusparam
  determine what effect is used, appear 22 times, so probably useless

- playmusic: start a bgm
- musicvolume: adjust the bgm volume
- stopmusic: stop the bgm

- playsound: same for sfx
- soundvolume: have apparently missing values?
- stopsound

- curtain: fill a part of the screen (defined by params)

- effect: vfx
- cameraeffect
- camerashake

- avgdisplay
  avg control

- theater
  set theater mode

- video
  play a video

- delay

- background: set the background, bare to clear the bg
- bgeffect: apply an effect on the bg, can be bare to clear the effect

- gridbg: load a grid of bgs. bare to clear the bg
- largebg: load multiples bgs in a strip (for panoramas), bare to clear
- verticalbg: load multiples bgs in a vertical strip, bare to clear ig

- image: fullscreen image, bare to clear
- imagerotate: rotate the current image
- imgeffect: effect (screen distortion or gate open in babel) bare to clear

- characteraction: animate a sprite

- imagetween: animate a property
- backgroundtween
- largebgtween
  missing params or missing diration -> delete

- interlude: way to apply a mask or an effect, ig, have lots of params

- charactercutin: phone transmission (char in a box)

- timersticker: displays a timer
- timerclear

- spellsticker: display an effect overlay (only on ch 17, pretty new)
- spellstickerclear

- decision: doc dialog options options separated by ;
- predicate: skip node for options references say if the following text should be displayed
