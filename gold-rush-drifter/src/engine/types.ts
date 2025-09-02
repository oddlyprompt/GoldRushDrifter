export type Rarity='common'|'uncommon'|'rare'|'epic'
export interface Item{ id:string; type:'weapon'|'hat'|'coat'|'boots'|'trinket'; name:string; rarity:Rarity; value:number; affixes:{id:string;value:number}[]; meta?:Record<string,any>; }
export interface Curio{ id:string; type:'curio'; name:string; value:number }
export interface Material{ id:string; type:'material'; tier:number; name:string; value:number }
export interface Actor{ id:string; kind:string; hp:number; maxHp:number; ai:'aggressive'|'skirmisher'|'sniper'; evasion:number; acc:number; dmg:[number,number]; status:string[] }
export interface Player{ name:string; hp:number; maxHp:number; grit:number; marksmanship:number; cunning:number; coin:number; reputation:number; ammo:{revolver:number;reserve:number}; status:string[]; inventory:(Item|Curio|Material)[]; equipped:{weapon:string|null;hat:string|null;coat:string|null;boots:string|null;trinket:string|null} }
export interface Building{ id:string; tier:1|2|3; unlocked:boolean }
export interface Town{ name:string; prosperity:number; threat:number; buildings:Building[] }
export interface Room{ zone:'Town'|'Wilds'; id:string; actors:Actor[]; effects:string[] }
export interface Encounter{ id:string; type:'bounty'|'escort'|'prospect'|'duel'|'rescue'|'raid'; site:string; difficulty:0|1|2|3; ticks:number; objective:string; active:boolean }
export interface World{ time:number; tickSeconds:number; weather:string; event:{id:string;label:string;duration:number}|null; autoTickCap:number }
export interface GameState{ seed:number; rollIndex:number; world:World; flags:{autoTick:boolean;paused:boolean}; player:Player; town:Town; room:Room; encounter:Encounter|null; log:string[] }