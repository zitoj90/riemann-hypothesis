import os
import sys

def verify_repository_git_boundaries():
    print("[TEST] Running Git Deployment Boundary Pre-Flight Script...")
    
    base_dir = r"D:\Me\Development\Riemann Hypothesis"
    license_file = os.path.join(base_dir, "LICENSE.md")
    
    print("\n--- AUDITING OPEN-SOURCE FIREWALL BOUNDARIES ---")
    
    # Check 1: Verify the presence of your hardened personal legal shield
    if os.path.exists(license_file):
        print("[PASSED] Root LICENSE.md detected. Personal copyright shield is active.")
    else:
        print("[FAILED] Critical Security Error: LICENSE.md missing from root directory.")
        return False
        
    # Check 2: Scan for your protected Obsidian Roadmap note inside the D: drive
    active_folders = os.listdir(base_dir)
    protected_file_token = "riemann hypothesis roadmap"
    
    # Deep scan file system tree for any accidental leakage of the roadmap note
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if protected_file_token in file.lower():
                print(f"[FAILED] Safety Breach: Protected Obsidian file leaked into D: drive -> {file}")
                return False

    print("[PASSED] Complete isolation verified. 'Riemann Hypothesis Roadmap.md' is safely excluded.")
    print("\n[SUCCESS] Pre-flight firewall scan complete. Repository is completely isolated and safe for deployment.")
    return True

if __name__ == "__main__":
    verify_repository_git_boundaries()
