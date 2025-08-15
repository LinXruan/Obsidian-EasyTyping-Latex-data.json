# Obsidian-EasyTyping-Latex-data.json

## Powerful LaTeX Script data.json for the Full-Stack Obsidian Plugin Easy Typing — Significantly More Capable Than LaTeX Suite

### 1. Advantages
1. Lightning-fast input for nearly all LaTeX code  
2. Exceptionally comprehensive one-click smart deletion functionality, capable of handling even simple nested structures  
3. Intelligent one-click cursor jumps when clicking the 'o' character  
4. Additional UTF-8 special character LaTeX formats (e.g., α, ξ, ∫, ∑) tailored for perfectionists, significantly reducing token usage during AI communication. See `data_com_UTF-8.json` in releases.  

### 2. Minor Issues
1. Due to regex complexity in processing nested formats, the production `data.json` file is extremely intricate and difficult to modify manually. For customization:  
   Use `data_simple.json` and the Python script `generate.py` (both in releases).  
   Modify `data_simple.json`, then run `generate.py` to regenerate `data.json`.  
   UTF-8 version generation is optional during this process.  

2. Easy Typing lacks environment detection, preventing exclusive activation within LaTeX environments. This causes frustration during English text entry. Solution:  
   Delegate input entirely to LaTeX Suite using `LatexSuite.txt` or `LatexSuite_UTF-8.txt` (copy to LaTeX Suite).  
   Use minimal `data.json` with only deletion + 'o' jump functions (`data_base.json` or `data_base_UTF-8.json`).  

### 3. File Inventory
**Complete Editions**  
- Standard: `data_com.json`  
- UTF-8: `data_com_UTF-8.json`  

**Base Editions (Deletion + 'o' Jump Only)**  
- Standard: `data_base.json`  
- UTF-8: `data_base_UTF-8.json`  

**Simplified Templates**  
- Complete: `data_simple_com.json`  
- Base: `data_simple_base.json`  

**LaTeX Suite Input**  
- Standard: `LatexSuite.txt`  
- UTF-8: `LatexSuite_UTF-8.txt`