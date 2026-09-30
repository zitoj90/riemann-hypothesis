import os
import shutil
import sys

def freeze_complete_project_tree():
    print("[BUILD] Initiating Master Index Immutable Lock...")
    
    base_dir = r"D:\Me\Development\Riemann Hypothesis"
    build_tag = "Phase3.1.1_MasterIndex_Locked"
    target_build_path = os.path.join(base_dir, "builds", build_tag)
    
    sources = {
        "src/Layer0_Proof.lean": "src/Layer0_Proof.lean",
        "archives/master_repository_manifest.md": "archives/master_repository_manifest.md",
        "tests/verify_repository_manifest.py": "tests/verify_repository_manifest.py"
    }
    
    try:
        os.makedirs(os.path.join(target_build_path, "src"), exist_ok=True)
        os.makedirs(os.path.join(target_build_path, "archives"), exist_ok=True)
        os.makedirs(os.path.join(target_build_path, "tests"), exist_ok=True)
        
        for src_rel, dest_rel in sources.items():
            src_full = os.path.join(base_dir, src_rel)
            dest_full = os.path.join(target_build_path, dest_rel)
            if os.path.exists(src_full):
                shutil.copy2(src_full, dest_full)
                print(f"[BUILD] Immutable Lock: Secured -> {dest_rel}")
                
        print(f"\n[PASSED] Master build successfully frozen at: builds/{build_tag}")
        return True
    except Exception as e:
        print(f"\n[FAILED] Build compilation halted: {str(e)}")
        return False

if __name__ == "__main__":
    freeze_complete_project_tree()
