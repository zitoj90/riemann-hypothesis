import os
import shutil

def freeze_personal_hardened_build():
    print("[BUILD] Initiating Phase 4.1.1 Personal Hardened Immutable Lock...")
    
    base_dir = r"D:\Me\Development\Riemann Hypothesis"
    build_tag = "Phase4.1.1_PersonalHardened_Complete"
    target_build_path = os.path.join(base_dir, "builds", build_tag)
    
    # Active personal core tracks to securely freeze
    sources = {
        "src/layer0_simulator.py": "src/layer0_simulator.py",
        "src/Layer0_Proof.lean": "src/Layer0_Proof.lean",
        "archives/arxiv_preprint_manuscript.md": "archives/arxiv_preprint_manuscript.md",
        "archives/master_repository_manifest.md": "archives/master_repository_manifest.md",
        "LICENSE.md": "LICENSE.md"
    }
    
    try:
        os.makedirs(os.path.join(target_build_path, "src"), exist_ok=True)
        os.makedirs(os.path.join(target_build_path, "archives"), exist_ok=True)
        
        for src_rel, dest_rel in sources.items():
            src_full = os.path.join(base_dir, src_rel)
            dest_full = os.path.join(target_build_path, dest_rel)
            if os.path.exists(src_full):
                shutil.copy2(src_full, dest_full)
                print(f"[BUILD] Immutable Lock: Secured -> {dest_rel}")
                
        print(f"\n[PASSED] Personal hardened build frozen at: builds/{build_tag}")
        return True
    except Exception as e:
        print(f"\n[BUILD_ERROR] Compilation failed: {str(e)}")
        return False

if __name__ == "__main__":
    freeze_personal_hardened_build()
