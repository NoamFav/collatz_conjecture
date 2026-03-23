# 🔢 Collatz Conjecture

<div align="center">

<img src="https://img.shields.io/badge/python-3.10+-3776AB.svg?style=for-the-badge&logo=python" alt="Python">
<img src="https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge" alt="License">

**Visualization and exploration of the Collatz conjecture**

[Usage](#usage)

</div>

---

An interactive Python exploration of the Collatz conjecture — visualize sequences, full trees, and convergence patterns using Graphviz and matplotlib.

---

## Usage

```bash
# Visualize a single sequence
python3 collatz_app.py

# Generate the full Collatz tree
python3 coll.py
# Output: collatz.dot → render with Graphviz
dot -Tpng collatz.dot -o collatz_tree.png
```

---

## License

MIT — see [LICENSE](LICENSE).

---

<div align="center">
Made with ❤️ by <a href="https://github.com/NoamFav">NoamFav</a>
</div>
