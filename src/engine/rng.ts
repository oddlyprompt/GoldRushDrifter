export function mulberry32(seed: number){
  return function(){ let t = (seed += 0x6d2b79f5); t = Math.imul(t ^ (t>>>15), t|1); t ^= t + Math.imul(t ^ (t>>>7), t|61); return ((t ^ (t>>>14))>>>0)/4294967296; };
}
export const int = (rng:()=>number,min:number,max:number)=>Math.floor(rng()*(max-min+1))+min
export const choice = <T,>(rng:()=>number, arr:T[])=>arr[Math.floor(rng()*arr.length)]
export function weighted<T extends string>(rng:()=>number, table:Record<T,number>):T{const e=Object.entries(table) as [T,number][];const tot=e.reduce((s,[,w])=>s+w,0);let r=rng()*tot;for(const [k,w] of e){r-=w;if(r<=0)return k}return e[e.length-1][0]}