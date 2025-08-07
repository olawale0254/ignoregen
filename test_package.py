#!/usr/bin/env python3
"""Test script for IgnoreGen package."""

def test_imports():
    """Test all imports work."""
    try:
        from ignoregen import IgnoreGen, generate_gitignore, ProjectDetector
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_cli():
    """Test CLI functionality."""
    try:
        from ignoregen.cli import main
        print("✅ CLI import successful")
        return True
    except ImportError as e:
        print(f"❌ CLI import error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality."""
    try:
        from ignoregen import generate_gitignore
        content = generate_gitignore(['python'])
        assert '__pycache__/' in content
        assert '*.py[cod]' in content
        print("✅ Basic functionality working")
        return True
    except Exception as e:
        print(f"❌ Functionality error: {e}")
        return False

def test_templates():
    """Test template availability."""
    try:
        from ignoregen import IgnoreGen
        gen = IgnoreGen()
        templates = gen.get_available_templates()
        expected = ['python', 'nodejs', 'react', 'django', 'java', 'cpp', 'base']
        for template in expected:
            assert template in templates, f"Missing template: {template}"
        print(f"✅ All {len(templates)} templates available")
        return True
    except Exception as e:
        print(f"❌ Template error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing IgnoreGen Package\n")
    
    tests = [
        test_imports,
        test_cli,
        test_basic_functionality,
        test_templates,
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 Package is ready for publishing!")
    else:
        print("❌ Fix issues before publishing")
