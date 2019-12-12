function isUnique(s){
  var hash = {};
  for (var i = 0; i < s.length; i++){
    if (hash[val]){
      return false;
    }else{
      hash[val] = true;
    }
  }
  return true;
}

console.log(isUnique('hello') === false);
console.log(isUnique('rainbow') === true);