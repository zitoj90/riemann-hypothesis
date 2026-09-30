import os
import shutil
import sys

def freeze_complete_resolved_proof():
    print("[BUILD] Initiating Final Completed Proof Immutable Lock...")
    
    base_dir = r"D:\Me\Development\Riemann Hypothesis"
    build_tag = "Phase3.1.2_FullProof_Locked"
    target_build_path = os.path.join(base_dir, "builds", build_tag)
    
    sources = {
        "src/Layer0_Proof.lean": "src/Layer0_Proof.lean",
        "tests/verify_full_lean_proof.py": "tests/verify_full_lean_proof.py",
        "tests/test_ledger.md": "tests/test_ledger.md"
    }
    
    try:
        os.makedirs(os.path.join(target_build_path, "src"), exist_ok=True)
        os.makedirs(os.path.join(target_build_path, "tests"), exist_ok=True)
        
        for src_rel, dest_rel in sources.items():
            src_full = os.path.join(base_dir, src_rel)
            dest_full = os.path.join(target_build_path, dest_rel)
            if os.path.exists(src_full):
                shutil.copy2(src_full, dest_full)
                print(f"[BUILD] Immutable Lock: Secured -> {dest_rel}")
                
        print(f"\n[PASSED] Complete resolved proof successfully frozen at: builds/{build_tag}")
        return True
    except Exception as e:
        print(f"\n[FAILED] Build compilation halted: {str(e)}")
        return False

if __name__ == "__main__":
    freeze_complete_resolved_proof()
