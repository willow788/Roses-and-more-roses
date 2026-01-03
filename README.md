# 🌹 Roses and More Roses

> *"Every rose has its thorn, but these ones just have math"* — Inspired by Guns N' Roses (obviously)

<div align="center">

![Python](https://img.shields.io/badge/Python-100%25-blue?style=for-the-badge&logo=python&logoColor=white)
![Math](https://img.shields.io/badge/Math-Beautiful-ff69b4?style=for-the-badge)
![Turtle Graphics](https://img.shields.io/badge/Turtle-Graphics-green?style=for-the-badge)

**Because why not draw roses with code instead of picking them?  🎸**

</div>

---

## 🎨 What's This About?

Oh jesus, I'm finally getting the hang of this!  This repository is all about drawing mathematical rose curves using Python's turtle graphics.  No gardening skills required, just some trigonometry and a lot of `cos()` functions. 

Basically, I learned about these beautiful mathematical curves and thought, "hey, let's make the computer draw flowers for me!" So here we are.

---

## 🌺 The Roses

### 1️⃣ **Maurer's Rose** 
A geometric star-like pattern that looks like someone went wild with a spirograph.  It uses angular stepping to create those cool intersecting lines. 

- **361 points** connected in a specific order
- **71° step angle** because why not
- **15 petals** of mathematical glory
- **Color:** `#a20b4a` (that fancy pink-red vibe)

### 2️⃣ **Rhodonea Rose**
The classic rose curve that actually looks like flower petals.  Smooth, continuous, and oddly satisfying to watch being drawn.

- **1000 points** for that smooth curve action
- **40 petals** (because k=20 and it's even, so we get 2k petals)
- **Color:** `#c01502` (bold red energy)
- Adapts to your screen size like a responsible program

---

## 🚀 How to Run

```bash
# Clone this bad boy
git clone https://github.com/willow788/Roses-and-more-roses.git

# Navigate to the folder
cd Roses-and-more-roses

# Run Maurer's Rose
python "Python code/Maurer's Rose/maurer. py"

# Or run Rhodonea Rose
python "Python code/Rhodonea rose/rhodonea.py"
```

Sit back, relax, and watch the magic happen.  It draws slowly on purpose so you can actually see it being created. Very zen.  Very cool. 

---

## 📐 The Math Behind It

Both curves use the polar equation: 

```
r = cos(k × θ)
```

Where:
- `r` is the radius
- `θ` (theta) is the angle
- `k` determines the number of petals

**The difference? **
- **Maurer Rose:** Samples points at fixed angular intervals (like every 71°) and connects them
- **Rhodonea Rose:** Continuously traces the curve from 0 to 2π

Why are we storing the points in Maurer's Rose? Because we need to draw lines between these points in a specific order.  It's all about that connection pattern!

---

## 🎯 What I Learned

- How to use Python's turtle graphics without losing my mind
- Polar to Cartesian coordinate conversion (thanks, math class)
- The difference between Maurer and Rhodonea rose curves
- That `enumerate()` is actually pretty useful
- Screen tracing optimization for smoother animations

---

## 💡 Credits

- **GeeksforGeeks (GfG):** For teaching me what these curves actually are and the math behind them.  You guys are legends. 
- **GitHub Copilot:** For helping with documentation (because let's be real, writing docs is not my favorite part)
- **Me:** For everything else — the code, the debugging, the "why isn't this working" moments, and finally getting it to work

---

## 🎸 Why "Roses and More Roses"? 

Because I'm a Guns N' Roses fan and I needed a cool name for a repository about drawing roses.  Also, "Welcome to the Jungle of Mathematical Curves" felt a bit too extra. 

---

## 📝 Technical Stuff

- **Language:** Python 100%
- **Libraries:** `turtle`, `math`, `time`
- **Optimization:** Screen tracer disabled for smooth animations
- **Animation Speed:** Intentionally slow so you can watch the patterns form

---

## 🌟 Future Plans (Maybe)

- [ ] Add more rose curve variations
- [ ] Make it interactive (choose your own k value?)
- [ ] Different color schemes
- [ ] Save the drawings as images
- [ ] Maybe some fractals?  Who knows. 

---

## 📜 License

Do whatever you want with this code. Draw roses, learn math, impress your friends. Just don't blame me if you get hypnotized by the patterns.

---

<div align="center">

**Made with ❤️, Python, and a lot of trial and error**

*Oh jesus, I'm finally getting the hang of this* 😄

</div>
