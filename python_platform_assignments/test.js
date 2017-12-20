function romanNumeralsConverter (roman){
  romanTranslator = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000};
  var numericEquivelant = 0;
  for (var i = 0; i < roman.length; i++){
    if ((romanTranslator(i+1)/romanTranslator(1) > 2) || (romanTranslator(i+1)/romanTranslator(i)) < 3 ){
      numericEquivelant += (romanTranslator(i) + romanTranslator (i+1));
    }
    else if ((romanTranslator(i-1)/romanTranslator(1) > 2) || (romanTranslator(i-1)/romanTranslator(i)) < 3 ){
      numericEquivelant += (romanTranslator(i) - romanTranslator (i-1));
   }
    else {
    numericEquivelant += romanTranslator(i);
    }
  }
}

romanNumeralsConverter("M");