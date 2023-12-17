function f(x) {
    if (x < 0) {
      x -= 2*x
      return f(x)
    }
    if (x < 99) {
      return x
    }
    x -= 99
    return f(x)
  }
  
 console.log(f(-133333)) 