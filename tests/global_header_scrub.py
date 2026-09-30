import os

def mass_find_and_replace_multi_target():
    print("[INIT] Initiating Multi-Target Global Repository Header Scrub...")
    
    # Target workspace path partition
    base_dir = r"D:\Me\Development\Riemann Hypothesis"
    
    # Define an ordered mapping array to handle replacement priorities cleanly
    replacements = {
        "zCorSystems": "Jonathan Zito",
        "zCor_Layer0": "Jonathan_Zito_Layer0",
        "zCor": "Jonathan_Zito"
    }
    
    # Explicit files to sweep and clean up
    files_to_clean = [
        r"src\layer0_simulator.py",
        r"src\Layer0_Proof.lean",
        r"archives\milestone_2_draft.md",
        r"archives\arxiv_preprint_manuscript.md",
        r"archives\arxiv_preprint_outline.md",
        r"archives\master_repository_manifest.md",
        r"archives\project_deployment_guide.md"
    ]
    
    print("\n--- EXECUTING DEEP FILE CONTENT SCRUB ---")
    
    for relative_path in files_to_clean:
        full_path = os.path.join(base_dir, relative_path)
        
        if os.path.exists(full_path):
            try:
                # 1. Read file into memory
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                original_content = content
                
                # 2. Loop through replacement dictionary in order of priority
                for target, replacement in replacements.items():
                    if target in content:
                        content = content.replace(target, replacement)
                
                # 3. Stream data backward to disk only if a change occurred
                if content != original_content:
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"[PASSED] Cleaned and Overwritten: {relative_path}")
                else:
                    print(f"[SKIPPED] No target phrases found inside: {relative_path}")
            except Exception as e:
                print(f"[ERROR] Failed to compile text modifications for {relative_path}: {str(e)}")
        else:
            print(f"[WARNING] Missing path mapping: {relative_path}")
            
    print("\n[SUCCESS] Global multi-target header scrub complete. Personal copyright layer applied across all files.")

if __name__ == "__main__":
    mass_find_and_replace_multi_target()
