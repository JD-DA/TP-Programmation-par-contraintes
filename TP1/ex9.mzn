int: max=200;

array [1..25] of var 1..max: carres;

constraint carres[21]+carres[18]+carres[24]=carres[25];
constraint carres[21]+carres[22]+carres[23]=carres[25];
constraint carres[24]+carres[20]+carres[19]=carres[25];
constraint carres[23]+carres[15]+carres[16]+carres[19]=carres[25];
constraint carres[9]+carres[7]+carres[8]=carres[18];
constraint carres[4]+carres[7]+carres[3]=carres[9];
constraint carres[9]+carres[18]=carres[21];
constraint carres[5]+carres[7]=carres[8];
constraint carres[4]+carres[5]=carres[7];
constraint carres[4]+carres[1]=carres[5];
constraint carres[3]+carres[1]=carres[4];
constraint carres[1]+carres[5]+carres[8]=carres[11];
constraint carres[3]+carres[10]=carres[1]+carres[11];
constraint carres[22]+carres[10]=carres[21]+carres[9]+carres[3];
constraint carres[22]=carres[10]+carres[17];
constraint carres[17]=carres[10]+carres[11];
constraint carres[18]+carres[8]+carres[11]+carres[17]=carres[13]+carres[24];
constraint carres[24]=carres[13]+carres[20];
constraint carres[23]+carres[14]+carres[12]=carres[13]+carres[17]+carres[22];
constraint carres[13]+carres[11]=carres[6]+carres[20];
constraint carres[6]+carres[19]=carres[20];
constraint carres[6]+carres[16]=carres[20];
constraint carres[6]+carres[12]=carres[16]+carres[2];
constraint carres[23]=carres[14]+carres[15];
constraint carres[15]=carres[14]+carres[2];
constraint carres[14]=carres[12]+carres[2];
constraint carres[16]=carres[14]+carres[2];
%contrainte sur l'ordre 1<2<3...
%contrainte sur l'air A25=A1+A2+...
solve satisfy;
output ["  carre n°17 = \(carres[17])\n"];