# Contributing Guide

## 🎯 Ways to Contribute

1. **Bug Reports** - Found an issue? Open a GitHub issue with details
2. **Feature Requests** - Have an idea? Suggest it in discussions
3. **Code Improvements** - Submit pull requests with enhancements
4. **Documentation** - Help improve docs and guides
5. **Translations** - Help translate to other languages

## 🚀 Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment tool

### Step 1: Fork and Clone
```bash
git clone https://github.com/YOUR-USERNAME/yolo-vision.git
cd yolo-vision
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development tools
```

### Step 4: Run Tests
```bash
pytest tests/
```

### Step 5: Run Application
```bash
streamlit run yolo_tanima.py
```

## 📝 Code Style

We follow PEP 8 standards. Please:
- Use meaningful variable names
- Add docstrings to functions
- Keep functions small and focused
- Comment complex logic

### Linting
```bash
flake8 yolo_tanima.py
black yolo_tanima.py
isort yolo_tanima.py
```

## 🔄 Pull Request Process

1. **Create a feature branch**: `git checkout -b feature/amazing-feature`
2. **Make your changes** with clear commit messages
3. **Push to your fork**: `git push origin feature/amazing-feature`
4. **Open a Pull Request** with a detailed description
5. **Wait for review** and address feedback

### PR Requirements
- ✅ Code follows style guidelines
- ✅ Works on Python 3.8+
- ✅ Tests pass locally
- ✅ Includes relevant documentation updates
- ✅ No breaking changes (or documented with migration guide)

## 🐛 Bug Reports

Include:
- Python version and OS
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs
- Screenshots if relevant

## 💡 Feature Requests

Describe:
- What feature you want
- Why it would be useful
- How it could work
- Any implementation suggestions

## 📚 Documentation

- Update README.md for user-facing changes
- Update DEPLOYMENT.md for deployment changes
- Add inline code comments
- Include examples for new features

## 🤝 Community

- Be respectful and constructive
- Provide helpful feedback
- Help other contributors
- Share knowledge

## ✨ Ideas for Contribution

- [ ] Support for video file input
- [ ] Batch image processing
- [ ] Export detection results (JSON, CSV)
- [ ] Performance metrics dashboard
- [ ] Multi-language support
- [ ] Dark/light theme toggle
- [ ] Custom model support
- [ ] API endpoint wrapper
- [ ] Mobile app wrapper
- [ ] Real-time statistics

## 📧 Questions?

Open a discussion or contact maintainers directly.

---

**Thank you for contributing! 🎉**
