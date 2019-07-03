"""
Copyright 2006 by Gregory C. Ewing.
This is free software. It may be used, modified and
redistributed freely, and derivative works may be
created from it and distributed freely.

python quest.py [options]
	-f			Run full-screen (default)
	-w			Run windowed
	<width>x<height>	Screen or window size (default 1024x768)

"""
from binascii import a2b_base64
from cStringIO import StringIO
from gzip import GzipFile
data={
'arithmetic':(390, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   wIo>Z`v6`r!0M.hoy\\#   <k3xBy2[i9Pr\'-IP>]_y3KAvcnrU+Kdj7&,jx!duK)ye"h34[>8im, %4z]Cf(NBX#nA"m_]<;y&a4f!Xd%[ML`A(=~Az^9d]Z(`\'%yJxURpQDN5"#6MC~7kh$QL3!0ZJ4yHE5($uK|@+BMC|=k?PzGFI83G_q7fiM8X9_N5ec~g#iK3Q@EhT:+7WZlM,s+:T5/V JYo{x.|1CnNXo,Q479y;7Y"=y,*g],X,MbDq<$t$HueVPsQ,5<_3i a6"r(R(S{#[]]OqW;EHtL3ub(5Mh5xp6e&"\'&2\\_H     ew^$mO~XjJ4'),
'black':(242, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   D.,Fj$Utjr!7Dy6\\V=!   u0h6U0_~D1P*Yo^`88WGx>UHn<j` 5K&jp-3.9>(u`A 1B0s;$ `AlLZzjE"_=_Ka Rqe~&*6Pr6\'&f\'T|*wiD0:cv?A3"D9vaNr|i[`?T}6w%!r~{MQ\\~TV6'),
'bran':(395, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   a)=!c|*;`r!!bCA>Hd#   M$!e{,j3d:Ps:CQpznvcsQM215ApZ+iI4TgKeY3|&<qN^2ilK.N$*96AU:?-A <h4BcZ);jFABn"  zWB?lg{Y-*xugI_,gGF1\'1mQVMuvC1]2cs!f(7?|y6.#]Ro`k*,MSchyQw1,nikq\\HrFAR#ky0".SddBf7:-/.$(K)z;&oL@_%BVif" vjO1m`k4{%t{g<Qm-(-8JvEFAvmBQ_dU/=H>#6@of]5&E]`I$$\\m0t{KfR]6WdR>j*=/Msjq+^gh6Dc_ 6d](JI)r%6vmT1/SS\\czd2>2*%Wd>M~+}g!r~{MQ\\~TV6'),
'bunny':(346, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   {Uk${[;v!s!hfDTZ,z"   DEDL@.%D+APA$Mx\\8b*5v\\x&nPjvZI#E@l5fqoO,L1~ix`tDZ6o\'<)A5CF6h3o@o4![@bmrl!;?HaD8t`WM5m5JSWWH,^_5?_\\,Ud@Mn!$o.s\\BvECHgRR0f#qc7z:X?:LED+9SS-NW.CN^Dy#3OKMn[fQruQ"+A&VLcbs>^+JJ3[4vFqz$"06AUk bq-SP{bK@\'M$,9u(qVW[|@jQE"VyQ#LNSaZ%P77\'Zk0[]wHCBZ1Cn^+C{KgDMlDpDaU'),
'castle':(283, 'zR_P">\\f"=Js{X8TKTU   Qc yU3$V^# l&bY7x*b*  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   B#*YIkxW7s!.D|(Vuz!   DQc{H&0i(APIGv8Vu9L<ER+=s!I#cwrs1"d"ss>oh)B>pSd#@8j#Z>:.0:mMhJG"z,!/`r6iwNZ\'$!b,az\'*"%`(8"Q_: 9W)UGDahv+d#WL3R$p34fBqSnh$HJuL#,S]5?#2j4OYfy3HCHDShP+\'_L>|D>l&eDX1G?U1{KgDMlDpDaU'),
'coconut':(356, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>    >OhaFp<,s!J1oeV(*#    (h?N3=sK=PE(3l8,.5WZh_Z*SJf^c`Vk6A-v<rWi[Ugd9"$NbsEap6!/<4~|g31^LDPCtO)7:~%6s^1i[Gc08?)f^XB\'}j*X0<1jan\\-wT<\\S~|7JiXc,A22Mo3d "*NVwZ?[5IALmGw|.yAq8aD_\\+9i"/:M0;?!y(\'e}X}xN{ReW_s2cRif[}^"Tz(iE;HP}QL;&E-:^Q0IR((n1oRKUkmrPk%c@\\acQZ[2\'k:vBsGi]g8=;>CZTD6%ABH,\\BF?3`24/5'),
'cord':(368, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   r`:xPYz<,s!L*i.e#<#   mU>.D)jly7PHdqF2XH;@$f_6+kypyTc.jE"Weu\'M`8d"hT4Px\'A;^Am3&ZEt_ =,V%`,[^{XlRM;!z^Wsni#syE\\Wyl|2}X#|wk ey,H3q-F6#GF{|TaO6sR9jc5[SLi3e08&kS<9z$H:*-%h%bx_}mMal@|7})CqQASR(Goh\'Ge}.N@+ 0vgY,C,86mM*,;Y\\,RIhxBB,#S"q,/n_R+K8&9RYk(7g[h{egM*M3{qcRm1Y{*6V|H!On|jc\'QK5:GnbFe4;PT!r~{MQ\\~TV6'),
'cracker':(262, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   gz6w3>n}_r!Z8oYTN[!   SOi6U0_~D1Pk\\dbHGvwqz%M;-Qk!afKV*S |[dR_?6l7&.JaI3>.Zx?;KA^,cKZG,lex:2hi+l\'3[hf|98E%DJv6f<c%B`\\*m*J(C~O5,dn9"R{s!+!6M]{1I~iLGzV\':GJ8onL?k1?*#  S"9KxrUV\\(H'),
'door':(302, 'zR_P">\\f"=Js{X8TKTU   Qc yU3$V^# l&bY7x*b*  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   +,yyb|\\\\7s!A![@E>8"   pEBm*KIk(APh_PM!`/(%yeB&~6k}=9PbVF,VEa7nOv>\\Q~iG\'f&V@\'5^jD"Zjzk+.*QunjOnHa*:PjL)LdY$N[iX8udU%uaAD*KgP}:FqO<G/H4Q]Euju5U(k)UoW_b<u @3~a,W1? QqI% ]H/"}nQ1H.wLfH6wexR|S):(fV?bO2A;-M)B}8=-B?/,\\BF?3`24/5'),
'door_mask':(184, 'zR_P">\\f"=Js{X8TKTU   Qc yU3$V^# l&bY7x*b*  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   n@FHt>|.Bs!M6gC&nE     4lK4O5A-AP+ZaP}6s\\\'XQCH\\*"Jo:W, ,b;P#j1{Gi"{KgDMlDpDaU'),
'downstairs':(279, 'zR_P">\\f"=Js{X8TKTU   Qc yU3$V^# l&bY7x*b*  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   j]Osm9w"`r!MF~Z1wt!   6\\Z"cC7@>1P5^o#2?Nk~@_y";V{wbJGW=Hl7trh@{onf`vD3/`RX|w$p@c"KLLe=d\\|dwoKXjsi}mdAP#3nqjh}6kWW\\4X>]at)H85M;$|$G&h^"bl"A =Zi&)2q=(^Z47"!w*bYFwIh;4_iGb&vlFGIt$8Jll~y#oC( '),
'frame-corner':(656, 'zR_P">\\f"=Js{X8TKTU   rH=|:YQjn! J\'Bc&db,&  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   \'E1o4)On!s!|@67Cmn\'   3}DEZLeo\',PslA,)_39*RkV\'T@;K4bp^0SpGa0:pi;ae$}5\\1\'\'NgC[z7vl[H|$;fVeXxNeT?k_K-[9>&+NU!uj(6/ci1jP4,l1W"P/pgY\'!S_xmw/8QR_.f9sA~.O)[(fChFlncnkeE8qBGOY/9lgm0@\'HyA}78#/\'"h9C\\rp,jlbply^#.1zoM04KDA\':o/Q<qZ"mS2"7c0tZRAM !Mk\\a}.C+*>5(dcAZ>D$CrM`Id:o\'7lc^H~])2W@d>;o>)M(+o.G`"=]8T!4}JYd1H:CIDPuJ&O\\6sV0-Et7(\'@G<rFV~H1Fl)o/IK`7f.k,p-aS-ToP(?Hd.:T!\'VkDPUHnRc1WL{BXQ,\'NB8yKPj*^ :g#pMFaSwc9o)HrcFBnX1\'vOx<+w?|q(DzIV2PNt|#*g_3H].jw7Fn..@0.O-4`t"6yX.B1A*+^UNxcqUQwax[-~\'D<AVN8%KHI5VDwA0V<yg%B*X%]>dBN:|WuES4L1+z+q1{i^afJ;ZY6&w#EZ\\<LX^pJqa:8kTZ\\/0{\'75OGY;sW>zEWCb$pf-]bt>[-sW-::CQMB*#^siDPFB+(GL}8-doRe>AF"w2EWh+}0g~,w:>y+(EO;U(L?`iq1!r~{MQ\\~TV6'),
'frame-side':(537, 'zR_P">\\f"=Js{X8TKTU   rH=|:YQjn! J\'Bc&db,&  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   G$8F5|Qn!s!x>+/zmz%   N+fF^3bx*6PXO]:o\'*8eNP//\\~/+r49g.K32BE,tG+zeBptNEL!qC)HLO[Kd~HY-6DZ\'x>e6H\'.Kiy;K8[[.^~YQ%>9p^Zxf(kKfTh/2d)T3}<wJRarQ(u`)4zy_6uQt.:  e.<b(DZXIr]8&XwvL5A1|>4FIp@N02hlA,Ufc*hHmSD:%^8S-\'Oz~STh8$I?P7\'vE#+!M1QW>,Ui36`zqw_p"tF%ry^PPYsBZ}$z9=k{-Pey)%t?\'0PrbM?g:kwt%\\E.$0Nc>Hy0(l?,7Q^z+jO;\'"gZ_C}TM)WKs^RHi-ZIRF,m};"S7x=\'u"8C2n\\AV7e;zl\'Dhg&3A\'pEBxqj#V!.Naf86s$)#]TS>!2QH=Se@8<~v02QS$Dc%$ehW]Wqaen QR![#-=BD@S+NUUzx}mGQ!WMgvYd8j8%46;On!_aHBB$B`$RrYrKTH3/Uo\'Dc{O.>u K@GY*nH@H9;|W,\\I1B}}W1ZML{n*8'),
'french':(472, 'zR_P">\\f"=Js{X8TKTU   Qc yU3$V^# l&bY7x*b*  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   *?\\$F(wW7s!}L4LcXx$   b"4/ED[/A>P_J/[t5ZnIBZ2yNd}Z^?ZjC,7exqVm@$qjvbba{wQ>o.3zz* YY&,F* `(25mVhs7i- .%]Ywbj-{`2AO)*Nqz)~4??UcU{e3d7@q>D;I.6a>f+.\\ui<xf}VRY2pO 5\'!.GN%aYGDWPh0n?CE~Ll@QmqN/iE|YoeT(_|:Ws2S2:tt}Q5@`jt-L!t(\\N[xwbzI_ccPeb\'`p4xF8x)1(e]$\\}VH(BBa:bg>j,z<]!*x)fP}YVSn\\IB0*OQ8nK~k8L?2Em#$v6]\'\'vMUm"s4;L+pGCp{?\'hs5bp/*hK>U>hOg0H$(Df>3jqnZ/)n18n1DPl~m ]h/d95.e)[o=(St{}N\'D1L[2b\\QevEKaJw@0dB!&5lj5^usF.sZ$p;k[IR|}.,G{KgDMlDpDaU'),
'general':(379, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   9S$-v2\\!kr!>kKKjNL#   1Rqr\'};Al9P>u:(Brvj5_`>%tc>T$lA+X;z})WJ7(9E=5T1oGbzwMC[i9M)t]rp(GOBsB5e,tC)OaLO3ZAZ5l$%1!N""{tRPT"IaBD!j]nQSp9S6\\gD5&,Ut]5wnsm}=y?+SCM{,+<XiC=NiEv#K:Db.oA\\HiwPBH2fHHmE!Q|ozGNEi"XMsvm{8@sb*i"EMWX42mM4*|eq_8ZoJ"V:/ V9WC=~L$&>*}pG4F!=2`=%^.H)o(Z.Kl9har{>!hjogSrRXia,g_v<O^#`N~_>onL?k1?*#  S"9KxrUV\\(H'),
'grass':(1177, 'zR_P">\\f"=Js{X8TKTU   4f yU3$V^# FuCU\\\'`v"  $t78B}_csA!(kb[we1+8X4<`#<Sf$5\'Q70,a6uDRglrn;iuAL_o8frnigxJqGHm|lntE.VHbe>vlnCD1_mJ>s-gnN"FjDe[D\'gn| IsiM4y=an(^]~@hQJ7anV\\`(fP* N[na:u3=kGPG[n09x<bS &^Un,d"!5?RUWUnieAlaB_\\(/_tCVw8]|-"/_CBY!^EUb8)_N n,5`r32)_|}p5ZHKhH#_(\\&A1ch9B#_VZ)JVKAnX|^a8>U-f^?R|^07A^RN7thv^;tUi)iTEbv^irXrNQ-zxp^e>bV!=_Jrp^C@"CN@lQCJON}6N%[*#=JO|{9WJCbWSDO(ZNb!^ )MDOVXQkFFX]c>Oa6fv|`u.]>O05i CINcs8O;r}+yck4m8Oip!5?LDi$3OtN6@ufa:}2OCM9I;O:o4-O?xB-m:l?.-O|yax:>yF^e?(Xv$qX7wWe?VVy-7AoLn_?a4/9m[-}g_?032B3DeR~Y?;pFMi^#$xY?inIV/G[X/T?tL^aeax))T?CKaj+JQ^?N?N)vuadn/9N?|\'y~\'MGdOH?xR#cY8y4IH?VTBO\'<\'<y!0a2WZ]VDlr!001Zc#?|A*{/;nnnYY:r#{/ilqw~ArG:u/tJ\'$V\\0x3u/CI*-{DhMJo/N\'?8R_&~Co/|%BAwG^SZi/(cVLNb{$Ti/VaYUsJTYjc/R-c9F6\'*dc/0/#&s9415= ;l71JTQa.= ij::o<*7E7 tHOEFWGg>7 CGRNk? =U1 N%gYBZ=mN1 |#jbgBuBe+ (a~m>]3s^+ V_"wcEkHu% a=7#;`)yn% 0<:,`HaN&  q`m|}@h2!?ik@TDgT@cdCT^On_C:0qq1:!{e\'s<#CV6%<mZKcj$*D5 "4O}4eVQY- G3C)Xse;t# U<n,eEiC)  4K+P~x/i%  BKVOy{\'t"  UT-N8~3@?ZiCZ3GM06D6WT{F]1fWZaZ;:9 j:&<veQ8%\\s{i/:1>.-O&mNV*J\\L   o{(U~A=<`1 XNKu#+`i_B5KkrxR\'!q37CP+k}h}u%gM@s>BVLsj3po7,c+QLQD6-2 e^*KBt4)WnC*"hRp4?h^{,]y]:dL(zDGiL_UIdvZBGE`[lejY,5|ADd<j2Kupx23a\'u"jmnz*w&P0[d)|zz}oV[?QQwN4;|&TL;1_1p4T-Vr"*7mneA>};Y=KS.|\'Qw>NbZP%K!+P2vURm!Ui&bVjMpTN7(U@|-=iMp\'Z>)TMuCi{~@cX+.!9(cz`&6qdYU@IUNx~E0W%S.\\Oc#Um*q%2,K%(SxAmqP;V=1/+k-0%6|3VK: lHpEC&1<k5.X`1K|\\R\\\'$6Y]^y?(wsr|$d:~.j3<buGXlhLaAJ22ePKCE,B()>Hi0_Dd.+$~67v2\'nJSzIw7<hM5VI9vWG&A1-PA5'),
'gravel':(333, 'zR_P">\\f"=Js{X8TKTU   labxU3$V^# %un)Fl:N%  $t78B}_csA!sBN[we1+8X4=Rl;Sf$5\'Q7e%WP/uAl!an[4?=n<pVuU5Nqv>XA8X9i)9:Fca*=3`OLbs#Ycmc+Uk34XK#u*9@R<U&mNV*J\\L   o{(U~A=<`1 XNKu#+`i_B5KkrxR\'!q37CP+k}h}u%gM@s>BVLsj3po7,c+QLQD6-2 e^*KBt4)WnC34"eO5BH^4&]CnsEr0Z#4C@bb7$8ABGoJM Zasom\\FpYouS:064F}?]N8Nj@Q@0zCHs+SI6gdTaYGs*Z_3D7fT)0W DWf{M8$BfYKK@fO%7{_&KQ,]YHYo!.IVYp/CYh7vP)j=oKcvaEV#moetLBip?sM_KH,&%jBMX$S8Jll~y#oC( '),
'grenade':(377, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   @):O7,JtLs!}<|4XOI#   [lrnYAQPa:P,hyRu6g\\;j_H)GrU2k.D<:/XP}JKU/cW80"VpNr$RRrWSTD.GL``$\'9#K6+8[gXY{k8?"\'Tz)?=#I-aod#{sc{nH)fB1r-MY=ZHsn}:#&Wfj}bj1A?y2WAg,EZ^grg6z`*I!R^x/EgKHMn[:<x\\HT}v[<9fyoG&g8i.e&/N [7%:S53M]/Tq#Xws6X1qSSf:Y\\HW7$&eczOOf4m3W6a7r?N93GV`B{ReZD%S0"-|JygZR@{ZVDd~F.d>a*W]JV0itjv:<6Li!r~{MQ\\~TV6'),
'hedge':(358, 'zR_P">\\f"=Js{X8TKTU   labxU3$V^# %un)Fl:N%  $t78B}_csA!sBN[we1+8X4=Rl;Sf$5\'Q7e%WP/uAl!an[4?=n<pVuU5Nqv>XA8X9i)9:Fca*=3`OLbs#Ycmc+Uk34XK#u*9@R<U&mNV*J\\L   o{(U~A=<`1 XNKu#+`i_B5KkrxR\'!q37CP+k}h}u%gM@s>BVLsj3po7,c+QLQD6-2 e^*KBt4)WnC\'qUp0|I<cC$KWxb%w"EhvJcDDD/Z#4%%4 HjL&OD:5_?cR*=_2#\\8.l<9oyCcLy3`gz7\'ZBtZth|(a$&^_C*6w`/ka^.y;+Y" jI(3v!S0(:1GY\'b4R4J5^b_>-m4T%[>ZZJ@8_@89~GD?^$&I~1KG~<Lb}u?=jJ|wx4UNGDu+za]TS vLGNVhZKx4=ipj8qSl*P(V9vWG&A1-PA5'),
'hermit':(458, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   C\'#Ao8*yjr![%klB^c$   <jJ2Lxe\\%7P];nEw]];XQ@&Ho@p7D0~(HO<y0a~%k<n )#M#ZT8lU2_,im/wFh|Yn\\.WIT`f4`i5;R`\\kB6#GA\'S=/\\IdU=B\'MBiASE73CcB3;RusJZ(/-zf_t9Vo@:s1rQdy6juaIKv;{MO*;EYT-P\'#+~b)Lv6.Pnjk>OpuLFJWV.]8T,sQxGb0 B(PjHT$~i"7KgR6Nvx[TV)[R_c}%&5Uvu4Q1g\'7:8Y8Ge?co@f-}42wRYsVQrGL&0 d9fvlche/X5>/?\'Am5(<4H,p#{Z8Lfb\\R<eOViB6^rrY"1AMnS$xW4zDQ2h\\*V>:Ie*(}qKj_<KQ[>:tIY5Dg#R0(>6-$D{WIblGy!6gt`qEfHOO@le2/p1H(H!r~{MQ\\~TV6'),
'key':(288, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   NPhD=EA3Bs!~X2a$D#"   SLMIhUFg(AP(+VW!JV9,0gL1x80{~#F0@],NNP!Vz[a9b!%y;l(l2}C(8Au+*Mj>T\\h+2qF_/ben%f};SW%iXfp`DL <OBD9gta}Ihr5DdB]AS1eIEK+)&:(VSK,{46.E1JkO]PF;O(#s?/3("Mx `<f7l.faKf#Mn>"D8Jll~y#oC( '),
'key_mask':(251, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   >Uyyr]B3Bs!hV-=O#K!   SOi6U0_~D1PZ1-D1Z;xqz%:Yy|u82a2r@TBraFd)3\'**$T^:tR,Kv&APgDFF9-\\-\\*ks1XsqTrHBmyxF-&1L3_/LeF[2[=w[m+:\\m4d?9Q{"Qg:iKj- 1e&r!!r~{MQ\\~TV6'),
'knight':(365, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   UxVtZ~"mjr!{C#lIT7#   gntk,,`It8PRENIt-k=H;*]L~?kepH8wCoVTg|S+4:9X-2 FLxuGQ|$o>EM~J"P&[C}.v{KT1.,\'\'KJ619/qZH^7[`D*fmU7{5SVqCL-a/8A@eO;+XepNqO]G#;`>dc4C:fQ|A[WA2d5CWDWB69Rm^qSc)>5l7&{pc=kKl^%\\!PC:O^^?q@+;I1\'dYfm$r_!q,fK|@A=iP]mHt52L<+>h\\IMm+^TmxQ9g,n~o"m;|0x#a{]fan18}rwZvQm+GL8}kZpWPj.;,\\BF?3`24/5'),
'msw':(414, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   i-qRG42HUr!4?"Y-p!$   0V}"@A.R|7PT_,dv<OF5#hU)Z9/u9<fBLOOB3GBS#fq)2`J^\\N7^SxVcfO5 B`ogtl4,;PpXiug7KukBdvaq4V&.&)].c&I@P2dDx2]Xuo`hy(T{/wj wO|U&)rM,NR9CrV@$vQvK*PKu_1zaF&\\&ov*_<dk@X&Vw`,K ^slVfcZ=`BE)n.w{Zs$k<S=RY5&U#FW^V_ZrY8lJ9CcQ("h#f}UoT=_"3DvZV~"Q.S&)i/yG@4)XBuX`"Da<]Rv_gK`< fei>!,0(%(Am8.D.b&z#R&.2&(|\\@$P)>[u5tJ+[wVG/k.~qBg}F y}gaFAgW8Jll~y#oC( '),
'nun':(330, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   >O-B%ka:`r!&pL^\'3b"   0+jf!vBL+AP6w*ydo6- AJFFb0p4B~$VH17B6by.;@zck6MWPm6q]MJ:V5z%tx1DM*W;"f((VI1#4]:5p_L\'"_>S>^/>XONAO67gY#CE($v!BkN)&}8eFHLV,<fYg5H0)$2Euopg?4 #Bz5kuA\\bKwu=PfH`\\.&"S;cYBP+3(Vb_A7<b~(rxRRhgGU*%Z,jB8aKmyeaQ1=t`8P9ImclHC~=n61$#}}W1ZML{n*8'),
'parrot':(319, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   b{}KUu1z_r!4/jA"gQ"   {idtf=kJ+APAuSd54>5i|RrgCr-%wD<x?m4tp \\IX-!h7wyRXj4u<PDxlQB|-!X(YM.kWbfH9P\'#F&\'iLo @Vo_HddJwX;uvj,B\'soH#K~V/&\\UBMwt&`[cSXT;W]8$a#hi2m:=\\IS!U4w&r%G{\'1kN4}1AP2wO7rh)!,NxK;phx`y.8rvB/9(4\'LVi&@SWL`iXBUfNCs;z\\dno4R{KgDMlDpDaU'),
'player':(346, 'zR_P">\\f"=Js{X8TKTU   q\\?J7%_+3# v K2^ Pg*  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   h&Lwa&=4Ur!hfDTZ,z"   Fr.zyQWlV<P6E\\w*P\'Idh89:&3Ui]3f!*>"}(58}8 {\'WAl%[#0BBX\'THMrL<yi{!aXQ(z+gCc4rljhH9\'q}:CJ(D2} (\\mM4:\\qSF^L[M[GiRa\'2~^m52e!7qwNOWo;}h]m&/}&-wB%3Yc*Us/C"dRp637b1HI/UE|P&;f 0&XE42mbdlk@{^?oi5.D&kt7&)rBv\\A,|0<?-|0)l%v"bWM\'*uB5PAb+Z4mmvhW)!Ol-]AT9= {KgDMlDpDaU'),
'shrubber':(375, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   frdemj~pjr!]mM}EPF#   p"MGMqk}S<P4\\$-\\n>y" h#XUA>Kft 0ClSL?Y:N!q:YC!FICCUvagQ*Z*GKv!vuc*$l3<+1(YFZI\\ohf%)XAu9TdUujCfuBAI,-7f5doE|\\Q`9jp^#hoN6y5s*=TeY#l\\;g5`[>Hc1KJ%:ktx/lHc?)\'9gymRljG/%{;H=YxHnrh0sV(NlXN__rb;=a5R5AVR|Dy<H~8\\U.s;,H\\-<tUDJ0yn0XePxyOTYn4.GUn[*~F_g4G0hBXt,n}3x=29y{xI1B{3=@;QN+R G}LL<}}W1ZML{n*8'),
'spam':(322, 'zR_P">\\f"=Js{X8TKTU   -["J7%_+3# `swwU,NI%  $t78B}_csA!sBN[we1+8X4=Rl;Sf$5\'Q7e%WP/uAl!an[4?=n<pVuU5Nqv>XA8X9i)9:Fca*=3`OLbs#Ycmc+Uk34XK#u*9@R<U&mNV*J\\L   o{(U~A=<`1 XNKu#+`i_B5KkrxR\'!q37CP+k}h}u%gM@s>BVLsj3po7,c+QLQD6-2 d^*KBt4)WnCW}R[:}F[yB0$Gq#Tl:T\'n?H^:fliQF!|8Tu;-8 %wMw"h_G8FsVDCb;[U\'">wg,~r0}3mjwqT}]8D[^<s\\6>}kU7=Z:dP8<-tRKNtL(8839Fp$;M#hU[X)},cxr\'zR@Z(htb1w[^"o+Q%ji}y\'W>v x*#>9vWG&A1-PA5'),
'spanish':(356, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   -Gt`.qs2`r!J1oeV(*#   #wI|-#{*\\;P;%O$TX@|6hAA``jhIe|GL:E8ee97Z>3hKO&$jsSLzwiboLB,g]gm"l81y,oGRl3;A/HIDsHPo+3p6-=D$DkBNzLRVl!jOk;@L,gtcA.KjF%4ERdY%AhZfliMO3rG65HW/&PL6,VYxxaN3\\<C:l_wuM4oQW.xdFE-n^/C?eFyAEA u{{%z]28zQ3+hv[276<,!iMTyBB1-AD.L`<.<az-u y4/~t)rCoUFQT~|2fMtX>`Y!i(=1,\\BF?3`24/5'),
'stone':(322, 'zR_P">\\f"=Js{X8TKTU   labxU3$V^# %un)Fl:N%  $t78B}_csA!sBN[we1+8X4=Rl;Sf$5\'Q7e%WP/uAl!an[4?=n<pVuU5Nqv>XA8X9i)9:Fca*=3`OLbs#Ycmc+Uk34XK#u*9@R<U&mNV*J\\L   o{(U~A=<`1 XNKu#+`i_B5KkrxR\'!q37CP+k}h}u%gM@s>BVLsj3po7,c+QLQD6-2 e^*KBt4)WnCjk<P@;n:Z)+$(r#Tl:T\'n?tIrKTWl+\\y]}GZ?]@&0=/;7a{%s\\#,Y|*sk_.ZlLzUq\',~VU3Mo"ElYgevf{<urA<dCwxQe8#:.}3W:#Fj;u}N3-8x(f6A~ySyMJjy+_+@^?&PY93#6@U$r7eWjXOtQHie;G9vWG&A1-PA5'),
'swallows':(380, 'zR_P">\\f"=Js{X8TKTU   2V^zwu:`f" "3c73Ufc$  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   ff\\Xjrk<,s!N#cVs}M#   flE)^zHJt8Pvhx%$|HC["#$rJ>77+1r3c/7#eFnY_HZN7&~]@L w>)jynEoF W+2w%Eloxkm(#R,E]~,euAf(Co*I2y|*?%Uo@EloZXY7ef-W@bOFk:7b]z#F7.\\niQHXg!aBH<F_Rn#9(,`<^tIU]WEJd}gMO3{8u]kex.AESaC8%%@UEk=ZO=6i&d`2+tbQ}V}74j"6#:;bDki@R}ehy$x-ve6<6\\4.dNld]Txf5M5R/8cr6k^:\\6~r:O.3G8x;Q# LlBWlZ4o\\j05({OUC`2MX.!   W]|US6A9be='),
'upstairs':(292, 'zR_P">\\f"=Js{X8TKTU   Qc yU3$V^# l&bY7x*b*  $t78B}_csA!+9M[we1+8X4{Jd+}Z66X;6C/g"M@~L,G#.-K(14D5y# \\{B0w2HWpsC-,O`VVd>u[>YnQ$/4NeWn.{`Ssx-|1a{)}&r*n=$>   /8KY=@b"`r!_V0/IB)"   `)z)Ox]\\3@P./bk\'M%i8=i,tviM&}#vX?wIuk-_v0A|Y+)XFZOjUzk&4-53GYx-f~,J`{`~XY Xg?~@6de@tV\'cWun0=%f|)(K$oW!)t\\_g&-G_ekq9~]9,oa(wl1_H"!w0!K4O32eO(9;"zzfU_x0n#R,2[Y^Hx^}MPBU,[<G=M=ky0{KgDMlDpDaU'),
}
VERSION="1.2"
dbg=False
import math,re,sys,textwrap
from getopt import getopt,GetoptError
from random import randrange,choice,shuffle,seed
from binascii import a2b_base64
from cStringIO import StringIO
try:
 set
except NameError:
 from sets import Set as set
import pygame
from pygame import Rect,Surface
from pygame.draw import arc,polygon
from pygame.color import Color
from pygame.locals import QUIT,KEYDOWN,KEYUP,USEREVENT,FULLSCREEN
try:
 data
except NameError:
 data={}
pygame.font.init()
fon=pygame.font.get_default_font()
def gf(size,italic=False):
 return pygame.font.Font(fon,size,italic=italic)
def decode((size,data)):
 blocks=[]
 r9=xrange(9)
 for i in xrange(0,len(data),11):
  chars=data[i:i+11:]
  chars=chars[::-1]
  n=0L
  for C in chars:
   n=n*95+(ord(C)-32)
  buf=[]
  for j in r9:
   buf.insert(0,chr(n&0xff))
   n>>=8
  blocks.append("".join(buf))
 return"".join(blocks)[:size]
def fat(msg):
 sys.stderr.write("%s\n"%msg)
 sys.exit(1)
usg="""
Usage:
   python quest.py [options] [<width>x<height>]

Options:
   -f	       Full screen
   -w	       Windowed
   -s size   Level size: 1, 2 or 3
   -i        Skip instructions screen
"""
class Options:
 seed=None
 stk=0
 seh=False
 smd=False
 dts=None
 fu=True
 lvs=None
 ski=False
 def __init__(s):
  args=sys.argv[1:]
  try:
   opv,params=getopt(args,"fwis:HMS:L:")
   for opt,val in opv:
    if opt=="-f":
     s.fu=True
    elif opt=="-w":
     s.fu=False
    elif opt=="-i":
     s.ski=True
    elif opt=="-s":
     s.lvs=val
    elif opt=="-S":
     s.seed=1234+int(val)
    elif opt=="-L":
     s.stk=int(val)
    elif opt=="-H":
     s.seh=True
    elif opt=="-M":
     s.smd=True
   if params:
    s.sws(params[0])
  except(GetoptError,ValueError):
   fat(usg)
 def sws(s,val):
  nums=[int(x)for x in val.split("x")]
  if len(nums)<>2:
   raise ValueError
  s.dts=nums
opts=Options()
dds=(1024,768)
if opts.smd:
 rmw=7
 rmh=7
 rmg=1
else:
 rmw=9
 rmh=9
 rmg=5
mnrw=5
mnrh=5
cw=32
ch=32
tibs=600,460
tif1=gf(96)
tif2=gf(24)
tif3=gf(48)
titc=Color("Gold")
tibg=Color("blue")
vef=gf(12)
stw=260
stlm=12
sttm=8
sttc=Color("black")
stwc=Color("red")
stbg=Color("wheat")
stf=gf(20)
stp=230
invf=gf(15)
lli=4
lf=gf(16)
llm=12
lhm=16
lvm=8
lotc=Color("black")
ltc=Color("brown")
lbgc=Color("wheat")
winf=gf(48)
vif=gf(24)
witc=Color("gold")
wibg=(100,0,0)
ripf=gf(96)
riptc=Color("black")
ripbc=Color("light grey")
scf=gf(96)
sctc=Color("black")
scbg=Color("lemonchiffon1")
scww=60
paf=gf(16)
ft=100
rptd=3
rpts=1
ibs=tibs
iclr=(100,0,0)
ibgc=Color("lemonchiffon2")
itf=gf(48)
ifnt=gf(20)
iww=50
ins="""
	Use the arrow keys to move around. To pick up an object,
	walk over it. To attack an enemy, try to walk into it.

	To use an item in your inventory, press the key indicated
	in (...) after the item's name. Some items may have more
	than one use, depending on the circumstances.

	Press M to see a map of the explored parts of the
	current level.

	Press ESCAPE during play to see these instructions again.
"""
opbs=(300,200)
ophf=gf(24)
opf=gf(18)
dszs={"1":("Small",(3,3)),"2":("Medium",(4,4)),"3":("Large",(5,5))}
crbs=640,300
crhf=gf(48)
crrf=gf(20)
crnf=gf(16,italic=True)
crtc=Color("gold")
credits=[["Concept and Programming",["Gregory Ewing"]],["Testing",["Oliver Hunt"]],["Attempted Testing",["Michael JasonSmith"]],["Acknowledgements",["The Monty Python Team"]],]
clrs={}
def ic():
 from pygame.colordict import THECOLORS
 n2n={}
 for key in THECOLORS:
  S=re.split("([0-9]+)",key)
  if len(S)>=2:
   nm=S[0]
   num=int(S[1])
  else:
   nm=S[0]
   num=0
  nums=n2n.setdefault(nm,[])
  if num:
   nums.append(num)
 nms=n2n.keys()+["almond","cream","lemon","rose"]
 wds1=set(nms)
 wds1.remove("gold")
 while 1:
  wds2=set()
  for wd1 in wds1:
   for w2 in wds1:
    if wd1<>w2:
     i=wd1.find(w2)
     if i>=0:
      w1a=wd1[:i]
      w1b=wd1[i+len(w2):]
      if w1a:
       wds2.add(w1a)
      wds2.add(w2)
      if w1b:
       wds2.add(w1b)
      break
   else:
    wds2.add(wd1)
  if wds2==wds1:
   break
  wds1=wds2
 for inm in n2n:
  nm=inm
  wds=[]
  while nm:
   for wd in wds2:
    if nm.startswith(wd):
     wds.append(wd)
     nm=nm[len(wd):]
     break
   else:
    wds.append(nm)
    break
  dnm=" ".join(wds)
  nums=n2n[inm]
  if nums:
   nums.sort()
   num=nums[len(nums)//2]
   inm="%s%s"%(inm,num)
  clrs[dnm]=THECOLORS[inm]
def icn():
 global avc
 avc=clrs.keys()
 shuffle(avc)
class Window(object):
 def __init__(s,mxw,mxh):
  lh=lli*lf.get_linesize()+2*lvm
  cwd=(mxw-stw)//cw
  chi=(mxh-lh)//ch
  ar=Rect(0,0,cwd*cw,chi*ch)
  lr=Rect(0,ar.bottom,ar.width+stw,lh)
  str=Rect(ar.right,ar.top,stw,ar.height)
  stm=str.inflate(-stlm,-sttm)
  scrr=ar.unionall([lr,str])
  s.cwd=cwd
  s.chi=chi
  s.ar=ar
  s.lr=lr
  s.str=str
  s.stm=stm
  s.scrr=scrr
  s.sl=0
  s.st=0
 def vp(s,lvl):
  rmi=s.st
  cmi=s.sl
  return(max(rmi,0),max(cmi,0),min(rmi+win.chi,lvl.dcw),min(cmi+win.cwd,lvl.dch))
 def rvlr(s,left,top,right,bottom):
  dr=dc=0
  vt=s.st
  vl=s.sl
  vr=vl+s.cwd
  vb=vt+s.chi
  if left<vl and right<vr:
   dc=-min(vl-left,vr-right)
  elif left>vl and right>vr:
   dc=min(left-vl,right-vr)
  if top<vt and bottom<vb:
   dr=-min(vt-top,vb-bottom)
  elif top>vt and bottom>vb:
   dr=min(top-vt,bottom-vb)
  vl+=dc
  vr+=dc
  vt+=dr
  vb+=dr
  s.sl=vl
  s.st=vt
DR=(0,1)
DD=(1,0)
DL=(0,-1)
DU=(-1,0)
dirs=(DD,DR,DU,DL)
wh=Color("white")
blk=Color("black")
KR=0x113
KD=0x112
KL=0x114
KU=0x111
KE=27
deg=math.pi/180.0
def load(imn,colorkey=wh):
 b95=data.get(imn[:-4])
 if b95:
  f=StringIO(decode(b95))
  image=pygame.image.load(f,imn)
 else:
  print"*** Loading image from file",imn
  image=pygame.image.load(imn)
 if colorkey:
  image.set_colorkey(colorkey)
 return image
fls=[load("gravel.png"),load("grass.png")]
wls=[load("hedge.png"),load("stone.png")]
ups=load("upstairs.png")
dnst=load("downstairs.png")
def cha(pct):
 return randrange(0,100)<pct
def fmt(msg,arg):
 if"%"in msg:
  msg%=arg
 return msg
def c2sc(r,c,w,h,map):
 r0=win.st
 c0=win.sl
 x=c*cw+(cw-w)/2
 y=r*ch+(ch-h)/2
 if not map:
  x-=c0*cw
  y-=r0*ch
 return x,y
def dti(surface,ti,r,c,map):
 if ti:
  w,h=ti.get_size()
  x,y=c2sc(r,c,w,h,map)
  surface.blit(ti,(x,y))
def dtt(surface,ti,mask,tnt,r,c,map):
 buffer=Surface(ti.get_size())
 buffer.set_colorkey(wh)
 buffer.fill(tnt)
 buffer.blit(mask,(0,0))
 buffer.blit(ti,(0,0))
 dti(surface,buffer,r,c,map)
def drt(surface,txt,font,color,center):
 image=font.render(txt,True,color)
 dst=image.get_rect()
 dst.center=center
 surface.blit(image,dst)
def gk(anm=None):
 while 1:
  event=pygame.event.wait()
  type=event.type
  if type==QUIT:
   sys.exit(0)
  elif type==KEYDOWN:
   return event.unicode.upper()
  elif type==USEREVENT:
   if anm:
    anm.upd()
    pygame.display.flip()
def gyn(anm=None):
 while 1:
  reply=gk(anm)
  if reply=="Y":
   return True
  elif reply=="N"or reply==chr(KE):
   return False
def gcoq(anm=None):
 while 1:
  key=gk(anm)
  if key in"\r\n\x03":
   return
  elif key=="Q":
   sys.exit(0)
class Frame(object):
 def __init__(s):
  from pygame.transform import flip,rotate
  s.topleft=load("frame-corner.png")
  s.topright=flip(s.topleft,True,False)
  s.botleft=flip(s.topleft,False,True)
  s.botright=flip(s.topright,False,True)
  s.top=load("frame-side.png")
  s.bottom=flip(s.top,False,True)
  s.left=rotate(s.top,90)
  s.right=flip(s.left,True,False)
  s.tsz=s.topleft.get_size()
 def draw(s,surface,rect):
  tw,th=s.tsz
  box=rect.inflate(tw,th)
  for x in xrange(box.left+tw,box.right-tw,tw):
   surface.blit(s.top,(x,box.top))
   surface.blit(s.bottom,(x,box.bottom-th))
  for y in xrange(box.top+th,box.bottom-th,th):
   surface.blit(s.left,(box.left,y))
   surface.blit(s.right,(box.right-tw,y))
  surface.blit(s.topleft,box.topleft)
  surface.blit(s.topright,(box.right-tw,box.top))
  surface.blit(s.botleft,(box.left,box.bottom-th))
  surface.blit(s.botright,(box.right-tw,box.bottom-th))
fra=Frame()
class AC(Exception):
 pass
class DGE(Exception):
 pass
class TC(object):
 surface=None
 lm=None
 color=None
 font=None
 tabs=None
 def __init__(s,surface,mar=0,top=0,color=None,font=None,ju=1):
  s.surface=surface
  s.mar=mar
  s.color=color
  s.font=font
  s.ju=ju
  s.x=mar
  s.y=top
 def write(s,txt=None,font=None,color=None,smooth=True,nl=False):
  font=font or s.font
  if txt:
   color=color or s.color
   image=font.render(txt,smooth,color)
   width=image.get_width()
   ju=s.ju
   if ju<0:
    s.x-=width
    x=s.x
   elif ju==0:
    x=s.x-width//2
   else:
    x=s.x
   s.surface.blit(image,(x,s.y))
   if ju>0:
    s.x+=width
  if nl:
   s.x=s.mar
   s.y+=font.get_linesize()
 def wl(s,*args,**kw):
  s.write(nl=True,*args,**kw)
class MessageLog(object):
 def __init__(s,rect):
  s.rect=rect
  s.mars=rect.inflate(-lhm,-lvm)
  s.cl()
 def cl(s):
  s.ls=[]
  s.tln=0
  s.markl=0
 def al(s,txt):
  s.ls.append(txt)
  s.tln=max(len(s.ls)-lli,s.tln)
 def mark(s):
  s.markl=len(s.ls)
 def draw(s,surface):
  surface.fill(lbgc,s.rect)
  tc=TC(surface,mar=win.lr.left+lhm,top=win.lr.top+lvm,font=lf,color=ltc)
  top=s.tln
  for i,li in enumerate(s.ls[top:top+4]):
   if top+i>=s.markl:
    color=ltc
   else:
    color=lotc
   tc.wl(li,color=color)
def log(msg):
 ml.al(msg)
class It(object):
 image=None
 nm=None
 shn=None
 pue=["","s"]
 snm=None
 tkm="You find %s."
 cmd=None
 iart="a"
 inc=False
 otp=False
 ipr=False
 is_obstacle=False
 plst=False
 nnw=False
 an=False
 lvj=0
 auxr=[]
 grpr=False
 scq=True
 som=False
 hidn=False
 prqf=None
 prqs=None
 lvl=None
 co=(0,0)
 sn=False
 def __init__(s,prqf=None):
  s.prqf=prqf
  s.prqs=[]
 def __str__(s):
  return"%s at %s of level %s"%(s.dn(),s.co,s.lvl)
 def gn(s,num=1,a=False,long=False):
  if long:
   nm=s.nm
  else:
   nm=s.shn or s.nm
  nm=fmt(nm,s.pue[num<>1])
  if a:
   art=s.iart
   if art=="a"and nm[0].lower()in"aeiou":
    art="an"
   nm="%s %s"%(art,nm)
  return nm
 def dn(s,long=False):
  return s.gn(long=long)
 def idn(s,long=False):
  return s.gn(a=True,long=long)
 def log(s,msg):
  log(fmt(msg,s.dn()))
 def gc(s):
  if s.lvl:
   r,c=s.co
   return s.lvl.gc(r,c)
  else:
   return None
 def gr(s):
  ce=s.gc()
  if ce:
   return ce.rm
  else:
   return None
 def atl(s,lvl):
  s.lvl=lvl
  if s.an:
   lvl.ani.append(s)
 def rmfl(s):
  lvl=s.lvl
  if s.an:
   lvl.ani.remove(s)
  r,c=s.co
  ce=lvl.gc(r,c)
  ce.it=None
  s.lvl=None
  s.co=None
 def mtc(s,r2,c2,nlv=None):
  lvl=s.lvl
  if lvl:
   r,c=s.co
   ce=lvl.gc(r,c)
   ce.it=None
  if nlv and nlv<>lvl:
   if lvl:
    s.rmfl()
   s.atl(nlv)
   lvl=nlv
  ce=lvl.gc(r2,c2)
  if not ce.floor:
   print"Item placed outside level %d:"%lvl.num,s
  if ce.wa:
   print"Item placed in wall:",s
  ce.it=s
  s.co=r2,c2
 def draw(s,surface,r,c,map):
  if not s.hidn:
   s.dti(surface,r,c,map)
 def dti(s,surface,r,c,map):
  dti(surface,s.image,r,c,map)
 def mks(s):
  if not s.sn and not s.hidn:
   s.sn=True
   s.rsn()
 def rsn(s):
  if s.snm:
   log(fmt(s.snm,s.idn(long=True)))
 def atk(s,ply):
  s.rtk()
  r,c=s.co
  s.rmfl()
  ply.ati(s)
  ply.stp2c(r,c)
  return True
 def rtk(s):
  log(fmt(s.tkm,s.idn()))
class TintedItem(It):
 def dti(s,surface,r,c,map):
  dtt(surface,s.image,s.mask,s.tnt,r,c,map)
class Ac(It):
 hl=None
 fo=None
 ho=True
 mob=True
 trng=3
 wch=10
 ctr=False
 hidn=False
 flo=False
 snm="You encounter %s."
 bm="The %s won't let you pass."
 atkm="The %s assaults you."
 hm="You assault the %s."
 msm="You swing at the %s, but miss."
 vms=["You have been defeated by %s."]*2
 dftm="The %s gives up and runs away."
 rvm="""Fortunately, you are found by a passing shrubber,
		who uses some of the supplies in your pack to restore your health
		with a nourishing meal of spam, bacon, sausages, eggs and spam."""
 def atl(s,lvl):
  It.atl(s,lvl)
  if s.flo:
   lvl.ga.acs.add(s)
  else:
   lvl.acs.append(s)
 def rmfl(s):
  if not s.flo:
   s.lvl.acs.remove(s)
  It.rmfl(s)
 def gvm(s,fat):
  return fmt(s.vms[not fat],s.idn(long=True))
 def grms(s):
  return s.rvm
 def atk(s,ply):
  if s.hidn:
   log("Something is blocking your way.")
  else:
   if s.ho:
    s.td(ply)
   else:
    s.log(s.bm)
 def td(s,ply):
  dmg=s.cdfp(ply)
  if dmg is not None:
   s.rdfp(dmg)
   if dmg>0:
    s.hl-=dmg
    if s.hl<=0:
     s.log(s.dftm)
     s.die()
   return dmg
  else:
   return 0
 def die(s):
  s.rmfl()
 def cdfp(s,ply):
  f=ply.fo
  return randrange(f//2,f+1)
 def rdfp(s,dmg):
  if dmg>0:
   s.log(s.hm)
  else:
   s.log(s.msm)
  if opts.seh:
   s.log("[%%s health is now %s]"%s.hl)
 def tt(s,ply):
  if s.lvl:
   dist=s.dstf(ply)
   if s.ho and s.iar(ply,dist):
    s.rvlp(ply)
    s.atkp(ply)
   elif s.mob:
    if dist<=s.trng:
     s.mtw(ply)
    elif cha(s.wch):
     s.ttmid(choice(dirs))
 def iar(s,ply,dist):
  return dist<=1
 def rvlp(s,ply):
  s.mks()
 def atkp(s,ply):
  dmg=s.cdtp(ply)
  s.rdtp(dmg)
  ply.td(dmg,s)
 def cdtp(s,ply):
  return randrange(1,s.fo+1)
 def rdtp(s,dmg):
  s.log(s.atkm)
 def ttmid(s,(dr,dc)):
  r,c=s.co
  r2=r+dr
  c2=c+dc
  ce=s.lvl.gc(r2,c2)
  if ce and not(ce.wa or ce.it or ce.sta):
   if not s.ctr or ce.rm:
    s.mtc(r2,c2)
 def mtw(s,ply):
  r,c=s.co
  pr,pc=ply.co
  if r<pr:
   r+=1
  elif r>pr:
   r-=1
  if c<pc:
   c+=1
  elif c>pc:
   c-=1
  ce=s.lvl.gc(r,c)
  if ce and not(ce.wa or ce.it or ce.sta):
   s.mtc(r,c)
 def dstf(s,ot):
  r1,c1=s.co
  r2,c2=ot.co
  return abs(r1-r2)+abs(c1-c2)
 def fli(s,ac,tol,pad=0):
  r,c=tol.rp(pad)
  ac.mtc(r,c,tol)
class Spam(It):
 image=load("spam.png")
 nm="tin%s of spam"
 cmd="S"
 lvj=50
 def use(s,ply):
  tgt=ply.gti()
  if isinstance(tgt,Shrubber):
   log("The shrubber accepts your payment and gives you a shrubbery.")
   ply.ati(Shrubbery())
  else:
   ply.ah(10)
   ply.af(5)
   log("You gobble a tin of spam.")
  ply.rmfi(s)
class MSW(Ac):
 image=load("msw.png")
 nm="Minister%s of Silly Walks"
 shn="minister%s"
 hl=5
 fo=4
 trng=2
 hm="You show the %s a silly walk of your own."
 atkm="The antics of the %s make you nearly laugh your head off."
 vms=["You have laughed yourself to death.","You have laughed yourself senseless."]
 dftm="The %s judges your walk worthy of a government grant."
 def atk(s,ply):
  if cha(30):
   log("The minister's antics paralyse you with laughter.")
  else:
   dmg=s.td(ply)
   if s.hl>0:
    if dmg<3:
     log('"It\'s not really very silly," he remarks.')
class Ca(It):
 image=load("castle.png")
 nm="abandoned castle%s"
 def atk(s,ply):
  log("There is a run-down French castle here.")
  log("Either there's nobody home, or they're not answering the door.")
class Fr(Ac):
 image=load("french.png")
 nm="upstart Frenchman%s"
 shn="Frenchman%s"
 hl=10
 fo=3
 mob=False
 nnw=True
 rude=["says something uncomplimentary about your mother","makes a scathing remark about English kaniggets","puts his thumbs in his ears and waggles his fingers at you","blows a raspberry at you","makes a rude gesture","farts in your general direction",]
 rsp=["You pointedly ignore him.","You aggressively ignore him.","You ignore him really hard.",]
 vms=["You have been mortally insulted by %s.","You have lost your temper with %s."]
 dftm="The %s retreats sullenly into his castle."
 rvm="""Fortunately, a passing shrubber intervenes
		and defuses the situation, preventing an international incident.
		But it takes two whole tins of spam to bring your blood
		pressure down to normal."""
 def iar(s,ply,dist):
  return s.gc().rm is ply.gc().rm
 def cdtp(s,ply):
  if cha(60):
   return Ac.cdtp(s,ply)
  else:
   return 0
 def rdtp(s,dmg):
  if dmg>0:
   adx=", hurting your feelings"
  else:
   adx=""
  s.log("The %%s %s%s."%(choice(s.rude),adx))
 def rdfp(s,dmg):
  msgs=s.rsp
  n=len(msgs)
  i=int((dmg*n)//11)
  log(msgs[min(i,n-1)])
 def die(s):
  r,c=s.co
  lvl=s.lvl
  Ac.die(s)
  castle=Ca()
  castle.mtc(r,c,lvl)
class Cracker(It):
 image=load("cracker.png")
 nm="cracker%s of resurrection"
 shn="cracker%s"
 cmd="C"
 lvj=50
 def use(s,ply):
  tgt=ply.gti()
  if isinstance(tgt,Pa):
   log("The cracker revives the parrot. It seems it was only resting.")
   tgt.rmfl()
   ply.rmfi(s)
   return True
  else:
   log("There's nothing here that wants a cracker.")
class Pa(Ac):
 image=load("parrot.png")
 nm="dead parrot%s"
 mob=False
 ho=False
 inc=True
 som=True
 auxr=[(Cracker,1,1)]
 grpr=True
 def atk(s,ply):
  s.log("The %s is blocking your path.")
class Ar(It):
 image=load("arithmetic.png")
 nm="arithmetic lesson%s"
 iart="an"
 cmd="A"
 scq=False
 def use(s,ply):
  log("Your counting ability makes a dramatic improvement.")
  ply.ain(5)
  ply.rmfi(s)
  return True
class Spa(Ac):
 image=load("spanish.png")
 nm="Spanish Inquisition%s"
 hidn=True
 hl=15
 fo=5
 wch=0
 atkm="The %s assails you with an almost fanatical devotion to the Pope."
 vms=["You have been fatally surprised by %s.","You have been surprised senseless by %s."]
 dftm='"We\'ll be back when you least expect it!" says the Inquisition as it departs.'
 def rvlp(s,ply):
  s.sn=True
  if s.hidn:
   s.hidn=False
   log("You are surprised by a Spanish Inquisition.")
 def cdfp(s,ply):
  i=ply.nu
  f=ply.fo//2
  if i>f:
   dmg=randrange(i//2,i+1)
   if i>=15:
    s.log("You bamboozle the %s with your brilliant counting skills.")
   else:
    s.log("You confuse the %s with your counting ability.")
  else:
   dmg=randrange(f//2,f+1)
   msg="You fend off the %s with brute strength."
   if i<=5:
    msg+=" Pity you can't count better..."
   s.log(msg)
  return dmg
 def rdfp(s,dmg):
  pass
class Br(It):
 image=load("bran.png")
 nm="packet%s of Pope Bran"
 cmd="B"
 lvj=50
 def use(s,ply):
  ply.amf(10)
  ply.rmfi(s)
  log("You wolf a packet of Pope Bran. Tasty, and it boosts your moral fibre.")
class Nu(Ac):
 image=load("nun.png")
 nm="attractive young nun%s"
 shn="nun%s"
 hl=5
 atkm="The %s plies you with dire temptation."
 vms=["You have been seduced by %s.","You were nearly seduced by %s."]
 dftm="The %s gives up and retreats in disappointment."
 rvm="""Fortunately, your fellows turn up just in time
		to rescue you from a fate better -- er, worse than death. You
		need two whole tins of spam to regain your composure."""
 auxr=[(Br,1,1)]
 grpr=True
 def cdfp(s,ply):
  mf=ply.mfb
  if mf>=5:
   return randrange(0,mf-3)
  else:
   log("You don't have the moral fibre to resist the nun's enticements.")
   return None
 def rdfp(s,dmg):
  if dmg>0:
   log("You valiantly fend off the nun's advancements.")
  else:
   log("Distracted by the nun's charms, you momentarily forget your resolve.")
 def atkp(s,ply):
  log("The nun plies you with dire temptation.")
  dmg=randrange(0,2)
  ply.amf(-dmg)
  if ply.mfb==0:
   ply.die(s)
class Shrubber(Ac):
 image=load("shrubber.png")
 nm="shrubber%s"
 mob=False
 ho=False
 ipr=True
 plst=True
 nnw=True
 scq=False
 som=True
 tih=0
 def atk(s,ply):
  s.tih+=1
  if s.tih>=10:
   log('"If that\'s how you feel, I\'ll go somewhere else."')
   s.fli(s,s.lvl)
   s.tih=0
   s.sn=False
  else:
   log("Assaulting an honest shrubber would hardly be chivalrous.")
   s.intrd()
 def rsn(s):
  log("You encounter a shrubber.")
  s.intrd()
 def intrd(s):
  log('"For my services, I require only a modest payment of spam," he says.')
class Shrubbery(It):
 nm="shrubber%s"
 pue=["y","ies"]
 cmd="G"
 def use(s,ply):
  tgt=ply.gti()
  if isinstance(tgt,Kn):
   tgt.ho=False
   tgt.sw-=1
   if tgt.sw>0:
    log('The knight says, "That\'s nice, but now I want... ANOTHER shrubbery!"')
   else:
    log('"What a lovely shrubbery! Thank you," says the knight, and lets you pass.')
    tgt.rmfl()
   ply.rmfi(s)
  else:
   log("There's nobody here who wants a shrubbery.")
class Kn(Ac):
 image=load("knight.png")
 nm="knight%s"
 hl=100
 fo=5
 mob=False
 inc=True
 scq=False
 som=True
 atkm='The %s says "Ni!" at you.'
 hm="You clash swords with the %s, and wound him a little."
 bm='"I want another shrubbery!" says the %s.'
 vms=["You have been Ni-ed to death by %s.","You have been Ni-ed unconscious by %s."]
 dftm="The knight succumbs to your relentless onslaught. If only there had been a better way..."
 auxr=[(Spam,2,2)]
 def __init__(s,*args,**kw):
  Ac.__init__(s,*args,**kw)
  s.sw=randrange(1,3)
 def rdtp(s,dmg):
  if cha(25):
   log('The knight says, "If you want me to let you through, bring me a shrubbery!"')
  else:
   Ac.rdtp(s,dmg)
 def cdtp(s,ply):
  return 1
class BN(Ac):
 image=load("black.png")
 nm="Black Knight%s"
 mob=False
 ho=False
 inc=True
 otp=True
 scq=False
 fo=10
 lms=None
 auxr=[(Spam,2,2)]
 def __init__(s,*args,**kw):
  Ac.__init__(s,*args,**kw)
  s.lms=["arm","arm","leg","leg"]
  shuffle(s.lms)
 def atk(s,ply):
  f=ply.fo-5
  if cha(30):
   s.log("The %s parries your thrust.")
  elif randrange(6)<=f:
   lim=choice(s.lms)
   count=s.lms.count(lim)
   if count>1:
    log("You lop off one of the Black Knight's %ss."%lim)
   else:
    log("You lop off the Black Knight's other %s."%lim)
   s.lms.remove(lim)
  else:
   s.log("Your swing fails to dent the %s's armour.")
  if s.lms:
   s.atkp(ply)
  else:
   if cha(50):
    log('"Come back here and fight like a man!" he yells as you walk past him.')
   else:
    log("He gnaws at your ankles as you step over him.")
   s.rmfl()
 def rdtp(s,dmg):
  arms,le=s.cntl()
  if le==2:
   if arms==2:
    s.log("The %s swings at you with his two-handed sword.")
   elif arms==1:
    s.log("The %s swings at you with his two^H^H^Hone-handed sword.")
   else:
    s.log("The %s kicks at you vicously.")
  elif le==1:
   if arms:
    s.log("The %s swings at you while balancing on one foot.")
   else:
    s.log("The %s hops and attacks you with a head-butt.")
  else:
   s.log("The %s takes a swipe at your knees.")
 def cntl(s):
  return s.lms.count("arm"),s.lms.count("leg")
 def gvm(s,fat):
  descs=[]
  for lim,adj in[("arm","armed"),("leg","legged")]:
   count=s.lms.count(lim)
   if count<2:
    descs.append("%s-%s"%(("no","one")[count],adj))
  if descs:
   desc=", ".join(descs)+" "
  return"You have been %s by a %sBlack Knight."%(("clobbered","killed")[fat],desc)
class GN(It):
 image=load("general.png")
 nm="scroll%s of general knowledge"
 cmd="K"
 ipr=True
 scq=False
 lvj=70
 def use(s,ply):
  log("You learn a variety of obscure and useless facts.")
  ply.agn(5)
  ply.rmfi(s)
class He(Ac):
 image=load("hermit.png")
 nm="mysterious hermit%s"
 shn="hermit%s"
 mob=False
 ho=False
 inc=True
 otp=True
 scq=False
 auxr=[(GN,3,3)]
 tpcs=None
 ans=0
 def __init__(s,*args,**kw):
  Ac.__init__(s,*args,**kw)
  s.rst()
 def rst(s):
  tpcs=["geography","history","physics","chemistry","biology","calculus"]
  shuffle(tpcs)
  s.tpcs=tpcs[:2]+["swallows"]
  s.ans=0
  s.sn=0
 def rsn(s):
  Ac.rsn(s)
  log('"Three questions shall ye answer before ye shall pass!" cackles the hermit.')
 def atk(s,ply):
  if s.ans<3:
   tpc=s.tpcs[s.ans]
   log("The hermit asks you an obscure question about %s."%tpc)
   if ply.gkn//5>s.ans:
    s.ans+=1
    if s.ans<3:
     log("You call upon your general knowledge and answer the question correctly.")
    else:
     log('"African swallow or European swallow?" you ask.')
     log('"I don\'t know that!" he replies, and is flung to a distant part of the dungeon.')
     s.fli(s,s.lvl,pad=1)
   else:
    log('"I don\'t know that!" you reply, and are flung to a distant part of the dungeon.')
    s.fli(ply,s.lvl.lva)
    s.rst()
  else:
   log('"Bugger off!" says the hermit.')
class Grail(It):
 nm="Holy Grail%s"
 an=True
 pts=[(0,0),(0,2),(1,5),(3,8),(5,10),(8,12),(8,20),(0,22),(0,24)]
 bc=Color("gold")
 dclr=0
 ddclr=7
 mxdc=40
 color=bc
 tkm="You've found the grail! Now all you have to do is get out of here alive..."
 def atk(s,ply):
  It.atk(s,ply)
  ply.hag=True
  ply.ga.rpopd()
 def draw(s,surface,r,c,map):
  x,y=c2sc(r,c,0,0,map)
  s.dra(surface,x,y,1)
 def dra(s,surface,x,y,sca):
  co1=[]
  co2=[]
  for px,py in s.pts:
   co1.append((x+(px-12)*sca,y+(py-12)*sca))
   co2.append((x+(12-px)*sca,y+(py-12)*sca))
  co=co1+co2[::-1]
  thick=(sca+1)/2
  polygon(surface,s.color,co)
  polygon(surface,blk,co,thick)
 def doa(s):
  d=s.dclr
  s.color=tuple([min(255,C+d)for C in s.bc])
  d+=s.ddclr
  s.dclr=d
  if d>=s.mxdc or d<=0:
   s.ddclr*=-1
class Bu(Ac):
 image=load("bunny.png")
 nm="vorpal bunny%s"
 hl=50
 fo=7
 mob=True
 trng=7
 ho=False
 snm="You come across a cute little bunny rabbit."
 hm="You strike desperately at the %s."
 atkm="The %s attacks you viciously."
 vms=["You have been mauled to death by %s.","You have passed out from loss of blood."]
 dftm="The %s seems to be dead (let's hope so, anyway)."
 auxr=[(Spam,-2,1)]
 atkd=False
 def atk(s,ply):
  if not s.ho:
   log("You reach out to give the bunny a pat.")
   s.ho=True
  else:
   Ac.atk(s,ply)
 def rdtp(s,dmg):
  if not s.atkd:
   log("It's a vorpal bunny! It attacks you vicously.")
   s.atkd=True
  else:
   Ac.rdtp(s,dmg)
 def tt(s,ply):
  Ac.tt(s,ply)
  if s.sn:
   s.ho=True
class K(TintedItem):
 image=load("key.png")
 mask=load("key_mask.png",blk)
 lvj=50
 def __init__(s,prqf):
  It.__init__(s,prqf)
  s.nm="%s key"%prqf.cn
  s.tnt=prqf.tnt
  prqf.key=s
class Do(TintedItem):
 image=load("door.png")
 mask=load("door_mask.png",blk)
 nm="door%s"
 inc=True
 scq=True
 som=True
 snm="You encounter %s."
 auxr=[(K,1,1)]
 def __init__(s,*args,**kw):
  It.__init__(s,*args,**kw)
  s.cn=avc.pop()
  s.nm="%s door"%s.cn
  s.tnt=clrs[s.cn]
 def atk(s,ply):
  if s.key in ply.inv:
   log("Fortunately you have a key for the %s."%s.dn())
   s.rmfl()
   ply.rmfi(s.key)
  else:
   s.log("You don't have a key for the %s.")
class Sw(Ac):
 image=load("swallows.png")
 nm="pair of swallow%s"
 ho=False
 mob=True
 wch=80
 ctr=True
 trng=0
 lvj=10
 flo=True
 scq=False
 cdr=(100,300)
 cot=None
 snm="A pair of swallows flitter by, without so much as a cord of line between them."
 def atk(s,ply):
  log("The swallows easily avoid you.")
 def tt(s,ply):
  Ac.tt(s,ply)
  t=s.cot
  if t is not None and t>0:
   t-=1
  if t==0:
   pr,pc=ply.co
   ce=ply.lvl.gc(pr,pc)
   rm=ce.rm
   if rm:
    for z in xrange(10):
     sc=ply.lvl.rpir(rm)
     cc=ply.lvl.rpir(rm)
     if sc and cc and sc<>cc:
      log("A pair of swallows fly into the room and drop a coconut.")
      r,c=sc
      s.mtc(r,c,ply.lvl)
      r,c=cc
      it=Coconut()
      it.mtc(r,c,ply.lvl)
      t=None
      break
  s.cot=t
class Cord(It):
 image=load("cord.png")
 nm="cord%s of line"
 cmd="L"
 lvj=10
 scq=False
 def use(s,ply):
  tgt=ply.gti()
  if isinstance(tgt,Sw):
   s.log("The swallows take the %s and fly off to hunt coconuts.")
   tgt.cot=randrange(*tgt.cdr)
   ply.rmfi(s)
   tgt.rmfl()
  else:
   s.log("There's nobody there who seems to want a cord of line.")
class Coconut(It):
 image=load("coconut.png")
 nm="coconut%s"
 cmd="N"
 def use(s,ply):
  log("You munch a coconut. Oodles of body-building nutrients!")
  ply.hl+=5
  ply.mxhl+=5
  ply.bf+=5
  ply.fo=min(ply.fo+5,ply.bf)
  ply.rmfi(s)
class Gr(It):
 image=load("grenade.png")
 nm="Holy Hand Grenade%s"
 cmd="H"
 def use(s,ply):
  log("One, two, FIVE!")
  ki=0
  pr,pc=ply.co
  for r in xrange(pr-1,pr+2):
   for c in xrange(pc-1,pc+2):
    if r<>c:
     ce=ply.lvl.gc(r,c)
     if ce:
      it=ce.it
      if isinstance(it,Ac):
       if dbg:
        print"Killing",repr(it)
       it.rmfl()
       ki+=1
  if ki:
   log("Well, that takes care of them.")
  else:
   log("There was nobody in range.")
  ply.rmfi(s)
class GA(object):
 def __init__(s,surface,x,y,sca):
  s.surface=surface
  s.x=x
  s.y=y
  s.sca=sca
  s.grl=Grail()
 def upd(s):
  s.grl.doa()
  s.grl.dra(s.surface,s.x,s.y,s.sca)
if opts.smd:
 from small_levels import lvr
else:
 lvr=[[(MSW,3,7),(Fr,1,1),(Spam,3,5),(Do,0,2)],[(MSW,5,10),(Pa,1,2),(Fr,0,1),(Spam,1,3),(Do,0,2)],[(MSW,0,8),(Pa,1,3),(Spa,2,4),(Fr,-1,1),(Br,1,3),(Spam,1,2),(Do,0,2)],[(MSW,0,6),(Pa,0,1),(Spa,3,7),(Nu,2,4),(Sw,1,1),(Ar,2,3),(Cord,1,1),(Spam,1,2),(Do,0,2)],[(MSW,0,5),(Pa,-1,1),(Spa,1,3),(Nu,3,7),(Kn,1,2),(Shrubber,1,1),(Gr,0,1),(Spam,1,2),(Do,0,2)],[(MSW,0,4),(BN,1,1),(Spa,0,3),(Nu,2,5),(Kn,1,2),(Sw,0,1),(Cord,1,1),(Spam,1,2),(Do,0,2)],[(MSW,0,3),(He,1,1),(Spa,0,2),(Nu,1,4),(Kn,0,1),(Gr,-2,1),(Spam,1,2),(Do,0,2)],[(MSW,0,5),(Bu,3,6),(Spa,0,1),(Nu,0,3),(Gr,-4,1),(Cord,-2,1),(Spam,1,2),(Do,0,2)],]
rprec=[(MSW,-3,10),(Spa,-3,8),(Spa,-3,8),(Nu,-3,5),(Bu,3,7),(Bu,3,7),(Bu,3,7),(Spam,0,2)]
class Ce(object):
 floor=None
 sta=None
 it=None
 wa=None
 rm=None
 rvld=opts.smd
 def draw(s,surface,r,c,map=False):
  if s.rvld:
   dti(surface,s.floor,r,c,map)
   if s.sta:
    dti(surface,s.sta,r,c,map)
   it=s.it
   if it and(not map or it.som):
    it.draw(surface,r,c,map)
   dti(surface,s.wa,r,c,map)
class Room(object):
 lvl=None
 co=None
 exs=None
 cors=None
 avp=None
 ctd=False
 c_o=False
 rvld=False
 dfs=None
 def __init__(s,ces,rmr,rc,lvl):
  s.lvl=lvl
  s.co=rmr,rc
  s.exs={}
  s.cors=[]
  floor=choice(fls)
  wa=choice(wls)
  width=randrange(mnrw,rmw+1)
  height=randrange(mnrh,rmh+1)
  left=rc*(rmw+rmg)+randrange(rmw-width+1)
  top=rmr*(rmh+rmg)+randrange(rmh-height+1)
  right=left+width
  bottom=top+height
  s.left=left
  s.top=top
  s.right=right
  s.bottom=bottom
  poss=[]
  for r,c in s.alc(0):
   ce=ces[r][c]
   ce.floor=floor
   if r==top or r==bottom-1 or c==left or c==right-1:
    ce.wa=wa
   else:
    poss.append((r,c))
   ce.rm=s
  shuffle(poss)
  s.avp=poss
 def __str__(s):
  return"room %s of level %s"%(s.co,s.lvl.num)
 def rcts(s):
  for cor in s.cors:
   rm=cor.orm(s)
   if rm.dfs<s.dfs:
    return rm
  return s
 def rbap(s):
  poss=[]
  for r,c in s.alc(1):
   ce=s.lvl.gc(r,c)
   if not(ce.sta or ce.it):
    poss.append((r,c))
  shuffle(poss)
  s.avp=poss
 def alc(s,pad):
  for r in xrange(s.top+pad,s.bottom-pad):
   for c in xrange(s.left+pad,s.right-pad):
    yield r,c
 def ge(s,dr,dc):
  eco=s.exs.get((dr,dc))
  if not eco:
   if dr:
    ec=randrange(s.left+1,s.right-1)
    if dr<0:
     er=s.top
    else:
     er=s.bottom-1
   else:
    er=randrange(s.top+1,s.bottom-1)
    if dc<0:
     ec=s.left
    else:
     ec=s.right-1
   eco=er,ec
   s.exs[dr,dc]=eco
  return eco
 def rco(s,pad=0):
  r=randrange(s.top+1+pad,s.bottom-1-pad)
  c=randrange(s.left+1+pad,s.right-1-pad)
  return r,c
 def repf(s,it):
  if it.nnw:
   pad=1
  else:
   pad=0
  return s.rep(pad)
 def rep(s,pad=0):
  if dbg:
   print"Getting random empty position in",s,"with pad",pad
   print"Room bounds are row",(s.top,s.bottom),"col",(s.left,s.right)
  d=pad+1
  for co in s.avp:
   r,c=co
   if(s.left+d<=c<s.right-d and s.top+d<=r<s.bottom-d):
    s.avp.remove(co)
    if dbg:
     print"Found",co
    return co
  if dbg:
   print"None found"
  return None
 def rvl(s,lvl):
  if not s.rvld:
   s.rvld=True
   for r in xrange(s.top,s.bottom):
    for c in xrange(s.left,s.right):
     lvl.gc(r,c).rvld=True
class Corridor(object):
 co=None
 rms=None
 c_o=False
 def __init__(s):
  s.co=[]
 def orm(s,rm):
  rms=s.rms[:]
  rms.remove(rm)
  return rms[0]
 def rcts(s):
  rm1,rm2=s.rms
  if rm1.dfs<rm2.dfs:
   return rm1
  else:
   return rm2
def mcp(lvl,path,thickness,proc,clct=None):
 for i in xrange(len(path)-1):
  r1,c1=path[i]
  r2,c2=path[i+1]
  top=min(r1,r2)
  bottom=max(r1,r2)
  left=min(c1,c2)
  right=max(c1,c2)
  for r in xrange(top-thickness,bottom+thickness+1):
   for c in xrange(left-thickness,right+thickness+1):
    ce=lvl.gc(r,c)
    if ce:
     proc(ce)
     if clct is not None:
      co=r,c
      if co not in clct:
       clct.append(co)
def mkc(lvl,path,floor,wa):
 def pw(ce):
  if not ce.floor:
   ce.floor=floor
   if not ce.wa:
    ce.wa=wa
 def ps(ce):
  ce.wa=None
 cor=Corridor()
 mcp(lvl,path,1,pw)
 mcp(lvl,path,0,ps,cor.co)
 return cor
def cr(lvl,rm1,rm2):
 rnr1,rc1=rm1.co
 rmr2,rc2=rm2.co
 dr=rmr2-rnr1
 dc=rc2-rc1
 er1,ec1=rm1.ge(dr,dc)
 er2,ec2=rm2.ge(-dr,-dc)
 path=[(er1,ec1)]
 if er1<>er2 and ec1<>ec2:
  if dr:
   m=(er1+er2)/2
   path.extend([(m,ec1),(m,ec2)])
  else:
   m=(ec1+ec2)/2
   path.extend([(er1,m),(er2,m)])
 path.append((er2,ec2))
 cor=mkc(lvl,path,choice(fls),choice(wls))
 rm1.cors.append(cor)
 rm2.cors.append(cor)
 cor.rms=[rm1,rm2]
 lvl.cors.append(cor)
def auc(lvl,rm):
 res=[]
 rmr,rc=rm.co
 for dr,dc in dirs:
  rm2=lvl.gr(rmr+dr,rc+dc)
  if rm2 and not rm2.ctd:
   res.append(rm2)
 return res
def mkrc(lvl):
 rm=lvl.rms[0][0]
 rm.ctd=True
 ca=[rm]
 while ca:
  rm=choice(ca)
  adj=auc(lvl,rm)
  if adj:
   rm2=choice(adj)
   cr(lvl,rm,rm2)
   rm2.ctd=True
   ca.append(rm2)
  else:
   ca.remove(rm)
def popl(lvls,rpop=False):
 pmts=[]
 for i,lvl in enumerate(lvls):
  if rpop:
   rec=rprec
  else:
   rec=lvr[i]
  expr(rec,lvl,pmts)
 shuffle(pmts)
 pootp(pmts)
 dipl(pmts)
 grpr(pmts)
 pfmp(pmts,rev=rpop)
def pootp(pmts):
 for i in xrange(len(pmts)):
  if pmts[i][1].otp:
   pmts.insert(0,pmts.pop(i))
def dipl(pmts):
 la=[]
 for pmt in pmts:
  if pmt[1].plst:
   la.append(pmt)
 for pmt in la:
  pmts.remove(pmt)
  pmts.append(pmt)
def grpr(pmts):
 liwc={}
 for lvl,it in pmts:
  if it.grpr:
   key=(lvl,it.__class__)
   if key in liwc:
    lit=liwc[key]
    it.prqs.extend(lit.prqs)
    del lit.prqs[:]
   liwc[key]=it
def expr(rec,lvl,pmts,prqf=None):
 sca=(lvl.rmsw*lvl.rmsh)/9.0
 for cls,lo,hi in rec:
  if not prqf and cls.scq:
   lo=int(round(sca*lo))
   hi=int(round(sca*hi))
  for j in xrange(randrange(lo,hi+1)):
   it=cls(prqf)
   pmts.append((lvl,it))
   if it.auxr:
    expr(it.auxr,lvl,it.prqs,prqf=it)
def pfmp(pmts,rev):
 while pmts:
  lvl,it=pmts.pop(0)
  if dbg:
   print"Performing placement of",it.dn(),"on",lvl
  pi(lvl,it,rev)
  if it.prqs:
   for prq in it.prqs:
    i=randrange(len(pmts)+1)
    pmts.insert(i,prq)
  if dbg:
   print"Performed placement of",it.dn()
def pi(lvl,it,rev):
 if it.prqf:
  pprq(it,rev)
 elif it.ipr:
  pirrf(it,lvl.enr,it.lvj)
 else:
  prgi(lvl,it)
def pprq(it,rev):
 pf=it.prqf
 if dbg:
  print"Placing prerequisite for",pf
 if pf.inc:
  fr=pf.cor.rcts()
 else:
  fr=pf.gr().rcts()
 if not rev:
  clch=it.lvj
 else:
  clch=0
 pirrf(it,fr,clch)
def pirrf(it,fr,clch):
 for rm in rchrs(fr,clch):
  if piir(it,rm):
   return
 print"*** No position found for",it
def prgi(lvl,it):
 while lvl.lva and cha(it.lvj):
  lvl=lvl.lva
 if it.inc:
  piicol(lvl,it)
 else:
  piirol(lvl,it)
def piicol(lvl,it):
 cor,co=lvl.rcp(it.otp)
 cor.c_o=True
 it.cor=cor
 piac(it,lvl,co)
def piirol(lvl,it):
 rmp=lvl.rrpf(it)
 if rmp:
  rm,co=rmp
  if it.is_obstacle:
   rm.c_o=True
  piirac(it,rm,co)
 else:
  print"*** No available position for",it
def piir(it,rm):
 co=rm.repf(it)
 if co:
  piirac(it,rm,co)
  return True
def piirac(it,rm,co):
 if dbg:
  print"Placing",it.dn(),"in",rm,"at",co
 piac(it,rm.lvl,co)
def piac(it,lvl,co):
 r,c=co
 it.mtc(r,c,lvl)
def rchrs(fr,clch):
 if dbg:
  print"Finding rooms reachable from room",fr.co,"of level",fr.lvl.num
 vstd=set()
 def trv(rm):
  if rm not in vstd:
   vstd.add(rm)
   if dbg:
    print"Room",rm.co,"of level",rm.lvl.num,"is a candidate"
   lvl=rm.lvl
   if rm is lvl.enr and lvl.lva and cha(clch):
    for rm2 in trv(lvl.lva.exr):
     yield rm2
   if rm is lvl.exr and lvl.lvb and cha(clch):
    for rm2 in trv(lvl.lvb.enr):
     yield rm2
   cors=rm.cors[:]
   shuffle(cors)
   for cor in cors:
    rm2=cor.orm(rm)
    if cor.c_o or rm2.c_o:
     if not rm2.dfs<rm.dfs:
      continue
    for rm3 in trv(rm2):
     yield rm3
   yield rm
 return trv(fr)
def cdfs(rm,d,rev):
 rm.dfs=d
 for cor in rm.cors:
  rm2=cor.orm(rm)
  if rm2.dfs is None:
   cdfs(rm2,d+1,rev)
  if rev:
   if rm2 is rm2.lvl.enr:
    lv2=rm2.lvl.lva
    if lv2:
     cdfs(lv2.exr,d+1,rev)
  else:
   if rm2 is rm2.lvl.exr:
    lv2=rm2.lvl.lvb
    if lv2:
     cdfs(lv2.enr,d+1,rev)
def rpopd(lvls):
 for lvl in lvls:
  lvl.cdf()
  lvl.rbap()
 cdfs(lvls[-1].exr,0,rev=True)
 popl(lvls[:-1],rpop=True)
class Level(object):
 ga=None
 num=None
 ces=None
 rms=None
 acs=None
 cors=None
 enco=None
 exco=None
 enr=None
 exr=None
 lva=None
 lvb=None
 ptl=None
 ani=None
 def __init__(s,ga,num,lva,(rmsh,rmsw)):
  s.rmsh=rmsh
  s.rmsw=rmsw
  s.dch=rmsw*rmw+(rmsw-1)*rmg
  s.dcw=rmsh*rmh+(rmsh-1)*rmg
  crng=xrange(s.dch)
  rrng=xrange(s.dcw)
  s.ga=ga
  s.num=num
  s.lva=lva
  if lva:
   lva.lvb=s
  s.acs=[]
  s.ani=[]
  ces=[[Ce()for c in crng]for r in rrng]
  s.ces=ces
  s.cors=[]
  s.rms=[[Room(ces,rmr,rc,s)for rc in xrange(rmsw)]for rmr in xrange(rmsh)]
  mkrc(s)
  s.enr,s.enco=s.ast(ups)
  if s.num<len(lvr)-1:
   ext=dnst
  else:
   ext=None
  s.exr,s.exco=s.ast(ext,exc=s.enr)
  s.ptl=s.fndp(s.enr,s.exr)
 def __str__(s):
  return"level %s"%s.num
 def cdf(s):
  for rm in s.alr():
   rm.dfs=None
 def agr(s):
  grl=Grail()
  r,c=s.exco
  grl.mtc(r,c,s)
 def ast(s,ti,exc=None):
  rm=s.rr(exc)
  co=rm.rep(pad=1)
  ce=s.gc(*co)
  ce.sta=ti
  return rm,co
 def fndp(s,fr,torm):
  path=[]
  vstd=set()
  def fpf(rm):
   vstd.add(rm)
   if rm is torm:
    return True
   else:
    for cor in rm.cors:
     rm2=cor.orm(rm)
     if rm2 not in vstd:
      if fpf(rm2):
       path.append(cor)
       return True
    return False
  if not fpf(fr):
   raise RuntimeError("No path from entrance to exit on level %d"%s.num)
  return path
 def fre(s,rec,rev=False):
  per=[(rec,False)]
  while per:
   rec,ipr=per.pop()
   for(cls,mnn,mxn)in rec:
    for i in xrange(randrange(mnn,mxn+1)):
     it=cls()
     s.ai(it,ipr,rev)
     aux=it.auxr
     if aux:
      per.append((aux,True))
 def plv(s,rev):
  if rev:
   return s.lvb
  else:
   return s.lva
 def gc(s,r,c):
  if 0<=r<s.dcw and 0<=c<s.dch:
   return s.ces[r][c]
  else:
   return 0
 def gr(s,rmr,rc):
  if 0<=rmr<s.rmsh and 0<=rc<s.rmsw:
   return s.rms[rmr][rc]
  else:
   return None
 def alr(s):
  for rmr in s.rms:
   for rm in rmr:
    yield rm
 def rr(s,exc=None):
  while 1:
   rm=choice(choice(s.rms))
   if rm is not exc:
    return rm
 def rp(s,pad=0):
  for z in xrange(100):
   rm=choice(choice(s.rms))
   r,c=rm.rco(pad)
   ce=s.gc(r,c)
   if not ce.it and not ce.sta:
    return r,c
 def rpir(s,rm,pad=0):
  for z in xrange(100):
   r,c=rm.rco(pad)
   ce=s.gc(r,c)
   if not ce.it and not ce.sta:
    return r,c
 def rrpf(s,it):
  if it.nnw:
   pad=1
  else:
   pad=0
  return s.rrp(pad)
 def rrp(s,pad):
  ca=list(s.alr())
  shuffle(ca)
  for rm in ca:
   co=rm.rep(pad)
   if co:
    return rm,co
  return None
 def rcp(s,otp=False):
  if otp:
   cors=s.ptl
  else:
   cors=s.cors
  ca=cors
  if ca:
   cor=choice(ca)
   return cor,choice(cor.co)
  else:
   print"*** No corridor position on path through level %d"%s.num
 def draw(s,surface):
  ces=s.ces
  rmi,cmi,rmx,cma=win.vp(s)
  rrng=xrange(rmi,rmx)
  crng=xrange(cmi,cma)
  for r in rrng:
   for c in crng:
    ces[r][c].draw(surface,r,c)
 def doa(s):
  for it in s.ani:
   it.doa()
 def rbap(s):
  for cor in s.cors:
   cor.c_o=False
  for rm in s.alr():
   rm.c_o=False
   rm.rbap()
 def shm(s,surface,box):
  bw=s.dch*cw
  bh=s.dcw*ch
  buffer=Surface((bw,bh))
  buffer.fill(blk)
  crng=xrange(s.dch)
  rrng=xrange(s.dcw)
  ces=s.ces
  for r in rrng:
   for c in crng:
    ces[r][c].draw(buffer,r,c,True)
  hs=float(box.width)/bw
  vs=float(box.height)/bh
  sca=min(hs,vs)
  surface.fill(blk,box)
  map=pygame.transform.rotozoom(buffer,0,sca)
  dst=map.get_rect()
  dst.center=box.center
  surface.blit(map,dst)
  pygame.display.flip()
  gk()
def lpi():
 right=load("player.png")
 left=pygame.transform.flip(right,1,0)
 up=pygame.transform.rotate(right,90)
 dwn=pygame.transform.flip(up,0,1)
 return{DR:right,DD:dwn,DL:left,DU:up,}
class Player(It):
 imgs=lpi()
 som=True
 lvl=None
 pos=None
 fa=DR
 hl=10
 mxhl=10
 fo=5
 bf=5
 nu=5
 mfb=5
 bmf=5
 gkn=0
 inv=None
 dmsg=None
 hag=False
 won=False
 lst=False
 dftd=False
 def __init__(s,lvl,(r,c)):
  s.inv=[]
  s.lvl=lvl
  s.mtc(r,c)
 def draw(s,surface,r,c,map):
  dti(surface,s.imgs[s.fa],r,c,map)
 def mo(s,(dr,dc),ir):
  r,c=s.co
  r2=r+dr
  c2=c+dc
  ce=s.lvl.gc(r2,c2)
  if not ce or ce.wa:
   raise AC
  it=ce.it
  if it:
   it.mks()
   if ir:
    raise AC
   it.atk(s)
  else:
   s.stp2c(r2,c2)
   s.rest()
 def stp2c(s,r,c):
  s.mtc(r,c)
  ce=s.lvl.gc(r,c)
  if ce and ce.sta:
   s.ust(ce.sta)
 def ust(s,sta):
  lvl=s.lvl
  if sta is ups:
   action="ascend"
   nlv=lvl.lva
   if nlv:
    r,c=nlv.exco
  else:
   action="descend"
   nlv=lvl.lvb
   r,c=nlv.enco
  if nlv:
   log("You %s the stairs."%action)
   s.mtc(r,c,nlv)
  else:
   if s.hag:
    log("You ascend the stairs... to victory.")
    s.won=True
   else:
    log("You can't leave now, you don't have the grail!")
 def mtc(s,*args):
  It.mtc(s,*args)
  s.swin()
 def swin(s):
  r,c=s.co
  ce=s.lvl.gc(r,c)
  rm=ce.rm
  if isinstance(rm,Room):
   win.rvlr(rm.left,rm.top,rm.right,rm.bottom)
  win.rvlr(c-2,r-2,c+3,r+3)
 def ati(s,it):
  s.inv.append(it)
 def rmfi(s,it):
  s.inv.remove(it)
 def ah(s,x):
  s.hl=max(0,s.hl+x)
 def af(s,x):
  s.fo=max(0,s.fo+x)
 def ain(s,x):
  s.nu+=x
 def amf(s,x):
  s.mfb=max(0,s.mfb+x)
 def agn(s,x):
  s.gkn+=x
 def rsth(s):
  s.hl=s.mxhl
  s.fo=s.bf
  s.mfb=s.bmf
  s.dftd=False
 def mte(s):
  if s.hag:
   co=s.lvl.exco
  else:
   co=s.lvl.enco
  s.mtc(*co)
 def td(s,dmg,ac):
  s.ah(-dmg)
  if s.hl<=0:
   s.die(ac)
 def die(s,ac):
  s.dftd=True
  fat=True
  sp=[x for x in s.inv if isinstance(x,Spam)]
  if len(sp)>=2:
   fat=False
   for x in sp[:2]:
    s.rmfi(x)
  s.dmsg=ac.gvm(fat)
  s.rvm=ac.grms()
  s.lst=fat
 def rest(s):
  if s.hl<s.mxhl:
   s.hl+=1
  if s.fo<s.bf:
   s.fo+=1
  if s.mfb<s.bmf:
   s.mfb+=1
 def pt(s):
  if s.hl>s.mxhl:
   s.hl-=1
  if s.fo>s.bf:
   s.fo-=1
  if s.mfb>s.bmf:
   s.mfb-=1
  for ac in s.lvl.acs:
   ac.tt(s)
 def gti(s):
  r,c=s.co
  dr,dc=s.fa
  ce=s.lvl.gc(r+dr,c+dc)
  if ce:
   return ce.it
  else:
   return None
 def unc(s):
  if s.dftd and not s.lst:
   return True
  else:
   return False
 def nbp(s):
  r,c=s.co
  for dr in xrange(-1,2):
   for dc in xrange(-1,2):
    if dr or dc:
     ce=s.lvl.gc(r+dr,c+dc)
     if ce and not ce.wa and not ce.it and not ce.sta:
      return r+dr,c+dc
  return None
k2d={KR:DR,KD:DD,KL:DL,KU:DU,}
class Ga(object):
 scr=None
 ply=None
 lvls=None
 acs=None
 lke=None
 rptc=0
 def __init__(s,scr,lvs):
  s.scr=scr
  s.acs=set()
  icn()
  numl=len(lvr)
  lvn=xrange(numl)
  lvls=[]
  ll=None
  for n in lvn:
   lvl=Level(s,n,ll,lvs)
   lvls.append(lvl)
   ll=lvl
  cdfs(lvls[0].enr,0,rev=False)
  ll.agr()
  popl(lvls)
  s.lvls=lvls
  lvl=lvls[max(-numl,min(opts.stk,numl-1))]
  s.ply=Player(lvl,lvl.enco)
  s.ply.ga=s
  ml.cl()
 def rpopd(s):
  rpopd(s.lvls)
 def run(s):
  ply=s.ply
  while 1:
   s.updv()
   s.refresh()
   if ply.won or ply.lst:
    break
   if ply.unc():
    s.dsc()
   else:
    s.h1e()
  if ply.won:
   anm=s.dvi()
  else:
   anm=s.ddf()
  return gyn(anm)
 def h1e(s):
  event=pygame.event.wait()
  type=event.type
  if type==QUIT:
   sys.exit(0)
  elif type==KEYDOWN:
   s.lke=event
   s.rptc=rptd
   return s.dkc(event,ir=False)
  elif type==KEYUP:
   s.lke=None
  elif type==USEREVENT:
   s.ply.lvl.doa()
   event=s.lke
   if event:
    s.rptc-=1
    if s.rptc==0:
     s.rptc=rpts
     return s.dkc(event,ir=True)
 def dkc(s,event,ir):
  try:
   if not ir:
    if s.dek(event):
     return
    elif s.dmapk(event):
     return
   ml.mark()
   if s.dmk(event,ir):
    s.pt()
    return
   if not ir:
    if s.dik(event)or s.dok(event):
     s.pt()
  except AC:
   pass
 def pt(s):
  s.ply.pt()
  for ac in s.acs:
   ac.tt(s.ply)
 def updv(s):
  ply=s.ply
  lvl=ply.lvl
  r,c=ply.co
  for dr in xrange(-1,2):
   for dc in xrange(-1,2):
    ce=lvl.gc(r+dr,c+dc)
    ce.rvld=True
    if not(dr or dc):
     rm=ce.rm
     if rm:
      rm.rvl(lvl)
    if dr and not dc or dc and not dr:
     it=ce.it
     if it:
      it.mks()
 def dvi(s):
  scr=s.scr
  box=Rect(0,0,500,400)
  box.center=win.ar.center
  scr.fill(wibg,box)
  fra.draw(scr,box)
  drt(scr,"Congratulations!",winf,witc,(box.centerx,box.top+60))
  drt(scr,"You escaped with the Holy Grail.",vif,witc,(box.centerx,box.bottom-70))
  drt(scr,"Play Again? (Y/N)",paf,witc,(box.centerx,box.bottom-30))
  pygame.display.flip()
  return GA(scr,box.centerx,box.centery,8)
 def dsc(s):
  ply=s.ply
  scr=s.scr
  box=Rect(0,0,520,310)
  box.center=win.ar.center
  scr.fill(scbg,box)
  fra.draw(scr,box)
  tc=TC(scr,mar=box.centerx,top=box.top+10,font=lf,color=sctc,ju=0)
  tc.wl("Ugh!",font=scf)
  tc.y+=20
  tc.wl(ply.dmsg)
  tc.y+=20
  msg=textwrap.wrap(ply.rvm.replace("\t",""),scww,expand_tabs=False,replace_whitespace=True)
  for li in msg:
   tc.wl(li)
  tc.y+=20
  tc.wl("Press ENTER to continue playing")
  pygame.display.flip()
  gcoq()
  ply.rsth()
  ply.mte()
 def ddf(s):
  scr=s.scr
  box=Rect(0,0,500,300)
  box.center=win.ar.center
  scr.fill(ripbc,box)
  fra.draw(scr,box)
  drt(scr,"RIP",ripf,riptc,(box.centerx,box.centery-50))
  drt(scr,s.ply.dmsg,lf,riptc,(box.centerx,box.bottom-100))
  drt(scr,"Play Again? (Y/N)",paf,riptc,(box.centerx,box.bottom-50))
  pygame.display.flip()
 def dek(s,event):
  if event.key==KE:
   shi(s.scr,"continue playing")
 def dmapk(s,event):
  if event.unicode.upper()=="M":
   s.ply.lvl.shm(s.scr,win.ar)
   return True
 def dmk(s,event,ir):
  dir=k2d.get(event.key)
  if dir:
   s.ply.fa=dir
   s.ply.mo(dir,ir)
   return True
 def dik(s,event):
  key=event.unicode.upper()
  for it in s.ply.inv:
   if it.cmd==key:
    it.use(s.ply)
    return True
 def dok(s,event):
  if event.unicode==" ":
   s.ply.rest()
   return True
 def refresh(s):
  scr=s.scr
  ply=s.ply
  lvl=ply.lvl
  scr.fill(blk,win.ar)
  lvl.draw(scr)
  ml.draw(scr)
  s.drs(ply)
  pygame.display.flip()
 def drs(s,ply):
  scr=s.scr
  scr.fill(stbg,win.str)
  mars=win.stm
  tc=TC(s.scr,mar=mars.left,top=mars.top,color=sttc,font=stf)
  tc.font=stf
  tc.tabs=[0,-stp]
  tc.wl("Level %d"%(ply.lvl.num+1))
  tc.y+=10
  tc2=TC(s.scr,mar=mars.right,top=tc.y,color=sttc,ju=-1,font=stf)
  def wst(lbl,val,base=None):
   valc=sttc
   if base is not None:
    tc2.write("/%d"%base)
    if val<=base//2:
     valc=stwc
   tc2.wl("%d"%val,color=valc)
   tc.wl(lbl)
  wst("Health",ply.hl,ply.mxhl)
  wst("Fortitude",ply.fo,ply.bf)
  wst("Moral Fibre",ply.mfb,ply.bmf)
  wst("Numeracy",ply.nu)
  wst("General Knowledge",ply.gkn)
  tc.y+=10
  tc.wl("Inventory")
  tc.y+=5
  tc.x=tc.mar
  tc.font=invf
  bags={}
  for it in ply.inv:
   bags.setdefault(it.gn(1,long=True),[]).append(it)
  keys=bags.keys()
  keys.sort
  for key in keys:
   bag=bags[key]
   count=len(bag)
   it=bag[0]
   desc="%d %s"%(count,it.gn(count,long=True))
   if it.cmd:
    desc="%s (%s)"%(desc,it.cmd)
   tc.wl(desc)
def id():
 global win,ml
 if not opts.dts:
  dw,dh=dds
  for mw,mh in pygame.display.list_modes():
   if mw>=dw and mh>=dh:
    w,h=mw,mh
  opts.dts=w,h
 w,h=opts.dts
 fl=0
 if opts.fu:
  fl|=FULLSCREEN
 else:
  h-=40
 win=Window(w,h)
 scr=pygame.display.set_mode(win.scrr.size,fl)
 pygame.display.set_caption("Quest")
 ml=MessageLog(win.lr)
 return scr
def sht(surface):
 rect=surface.get_rect()
 box=Rect(0,0,*tibs)
 box.center=rect.center
 surface.fill(tibg,box)
 fra.draw(surface,box)
 tc=TC(surface,mar=box.centerx,top=box.top+20,ju=0,color=titc)
 tc.wl("Quest",font=tif1)
 tc.wl("for the",font=tif2)
 tc.wl("Holy Grail",font=tif3)
 anm=GA(surface,box.centerx,tc.y+90,5)
 tc.y+=180
 tc.wl("Version %s"%VERSION,font=vef)
 tc.y+=20
 tc.wl("Press ENTER to continue",font=lf)
 pygame.display.flip()
 gcoq(anm)
def shi(surface,prompt):
 rect=surface.get_rect()
 box=Rect(0,0,*ibs)
 box.center=rect.center
 surface.fill(ibgc,box)
 fra.draw(surface,box)
 tc=TC(surface,mar=box.centerx,top=box.top+20,ju=0,color=iclr)
 tc.wl("How to Play",font=itf)
 tc.y+=30
 tc.font=ifnt
 for para in ins.replace("\t","").split("\n\n"):
  for li in textwrap.wrap(para,iww,replace_whitespace=True):
   tc.wl(li)
  tc.y+=10
 tc.y+=30
 tc.wl("Press ENTER to %s, Q to quit"%prompt)
 pygame.display.flip()
 gcoq()
def sho(surface):
 rect=surface.get_rect()
 box=Rect(0,0,*opbs)
 box.center=rect.center
 surface.fill(ibgc,box)
 fra.draw(surface,box)
 tc=TC(surface,mar=box.centerx,top=box.top+20,ju=0,color=iclr,font=opf)
 tc.wl("Select Level Size",font=ophf)
 tc.y+=20
 tc.ju=1
 tc.mar=tc.x=box.left+60
 tc2=TC(surface,mar=tc.mar+30,top=tc.y,ju=1,color=iclr,font=opf)
 keys=dszs.keys()
 keys.sort()
 for key in keys:
  nm,(rs,cs)=dszs[key]
  tc.wl(key)
  tc2.wl("%s (%s x %s)"%(nm,cs,rs))
 tc.y+=10
 tc2.y+=10
 tc.wl("Q")
 tc2.wl("Quit")
 pygame.display.flip()
 while 1:
  key=gk()
  if key=="Q":
   sys.exit(0)
  elif key in dszs:
   return dszs[key][1]
def dcr(scr):
 scr.fill(blk,win.scrr)
 w,h=crbs
 box=Rect(0,0,w,h)
 box.center=win.scrr.center
 tc=TC(scr,mar=box.centerx,top=box.top,color=crtc,ju=0)
 tc.wl("Credits",font=crhf)
 tc.y+=30
 for role,nms in credits:
  tc.wl(role,font=crrf)
  for nm in nms:
   tc.wl(nm,font=crnf)
  tc.y+=20
 pygame.display.flip()
 gcoq()
def main():
 if opts.seed is not None:
  seed(opts.seed)
 pygame.init()
 ic()
 scr=id()
 pygame.time.set_timer(USEREVENT,ft)
 try:
  sht(scr)
  if not opts.ski:
   shi(scr,"play")
  if opts.lvs:
   lvs=dszs[opts.lvs][1]
  elif opts.smd:
   lvs=(2,3)
  else:
   lvs=sho(scr)
  while 1:
   ga=Ga(scr,lvs)
   sys.stdout.flush()
   if not ga.run():
    break
 except SystemExit:
  pass
 if not opts.ski:
  dcr(scr)
main()
