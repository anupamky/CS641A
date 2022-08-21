def replac_(a,dic):
    ans=''
    for i in range(0,len(a)):
        j=a[i]
        if j in dic.keys():
            ans=ans+dic[j]
        else:
            ans=ans+j
    return ans
cip="wsam ie pjo ysgtm eyipbya .P axg niphay y,_mey syw ahgm ewhrg tw hmysyam wh meyiepjo_ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy_whmy sy amwh rmephmewagh y!Me yigu ynay utg_smew ajya apr ywap awjfkya no a mwmnmw_ghiwfeyswhve wieuwr wm aepby oyyhae wtmy_uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd_dvwmegnmmey dngmya. Mew awameyt"

c=0;
d=dict();
for j in range(0,len(a)):
    if cip[j].isalpha():

        i=cip[j].lower()
        c=c+1
        if i not in d.keys():
            d[i]=0
        else:
            d[i]=d[i]+1

for j in d.keys():

        d[j]=round(d[j]*100/(c),1);
print({k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)})

plain={"y":"e","m":"t","p":"a","e":"h","s":"r","w":"i","a":"s","f":"p","v":"w","g":"o","u":"d","n":"u","d":"q","i":"c","h":"n","k":"l","j":"m","o":"b","t":"f","b":"v","x":"y","r":"g"}

print()
print(replac_(cip, plain))
