#!/bin/bash
# Quick Overview of MAGI System v2.0

clear

cat << "EOF"
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                           MAGI SYSTEM v2.0                                   ║
║                        Project Overview                                      ║
║                                                                              ║
║                    MELCHIOR-1 • BALTHASAR-2 • CASPER-3                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
EOF

echo ""
echo "📊 PROJECT STATISTICS"
echo "════════════════════════════════════════════════════════════════════════════"
echo ""

# Count files
echo "📁 Files by type:"
echo "   Python scripts:     $(ls -1 *.py 2>/dev/null | wc -l)"
echo "   Documentation:      $(ls -1 *.md 2>/dev/null | wc -l)"
echo "   Launcher scripts:   $(ls -1 *.sh *.bat 2>/dev/null | wc -l)"
echo "   Config files:       $(ls -1 .env.example .gitignore requirements.txt 2>/dev/null | wc -l)"
echo ""

# Show main files
echo "🚀 MAIN EXECUTABLE FILES"
echo "════════════════════════════════════════════════════════════════════════════"
ls -lh magi_web_interface.py Main_core_002.py app.py test_setup.py 2>/dev/null | tail -n +2 | awk '{printf "   %-30s %6s\n", $9, $5}'
echo ""

echo "📚 DOCUMENTATION FILES"
echo "════════════════════════════════════════════════════════════════════════════"
ls -lh *.md 2>/dev/null | tail -n +2 | awk '{printf "   %-30s %6s\n", $9, $5}'
echo ""

echo "🔧 UTILITY SCRIPTS"
echo "════════════════════════════════════════════════════════════════════════════"
ls -lh launch_magi.* 2>/dev/null | tail -n +2 | awk '{printf "   %-30s %6s\n", $9, $5}'
echo ""

echo "⚙️  CONFIGURATION FILES"
echo "════════════════════════════════════════════════════════════════════════════"
ls -lh .env.example .gitignore requirements.txt 2>/dev/null | tail -n +2 | awk '{printf "   %-30s %6s\n", $9, $5}'
echo ""

# Total size
TOTAL_SIZE=$(du -sh . 2>/dev/null | cut -f1)
echo "💾 Total project size (excluding venv): $TOTAL_SIZE"
echo ""

echo "════════════════════════════════════════════════════════════════════════════"
echo ""
echo "📖 QUICK REFERENCES"
echo ""
echo "   🚀 Get started:           cat QUICKSTART.md"
echo "   📚 Full documentation:    cat README_v2.md"
echo "   🌐 Deploy guide:          cat DEPLOY_GUIDE.md"
echo "   🗂️  File structure:        cat PROJECT_STRUCTURE.md"
echo "   📝 What's new:            cat CHANGELOG.md"
echo "   🎯 Complete summary:      cat SUMMARY.md"
echo ""
echo "════════════════════════════════════════════════════════════════════════════"
echo ""
echo "🎯 QUICK START"
echo ""
echo "   1. Configure API keys:    cp .env.example .env && nano .env"
echo "   2. Test setup:            python test_setup.py"
echo "   3. Launch interface:      ./launch_magi.sh"
echo ""
echo "════════════════════════════════════════════════════════════════════════════"
echo ""
echo "✨ MAGI System v2.0 is ready for deployment!"
echo ""
echo "   Visit: http://localhost:7860 (after launch)"
echo ""
