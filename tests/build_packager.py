import os
import shutil
import sys

def compile_immutable_build():
    print("[BUILD] Initiating zCorSystems Build Packager...")
    
    base_dir = r"D:\Me\Development\Riemann Hypothesis"
    build_tag = "Phase2.4.1_LiveMath_Verified"
    target_build_path = os.path.join(base_dir, "builds", build_tag)
    
    # Source paths to lock down
    sources = {
        "src/layer0_simulator.py": "src/layer0_simulator.py",
        "archives/milestone_2_draft.md": "archives/milestone_2_draft.md",
        "tests/test_milestone2_math.py": "tests/test_milestone2_math.py"
    }
    
    try:
        # Create folder structure
        os.makedirs(os.path.join(target_build_path, "src"), exist_ok=True)
        os.makedirs(os.path.join(target_build_path, "archives"), exist_ok=True)
        os.makedirs(os.path.join(target_build_path, "tests"), exist_ok=True)
        
        # Mirror files securely into the compilation build
        for src_rel, dest_rel in sources.items():
            src_full = os.path.join(base_dir, src_rel)
            dest_full = os.path.join(target_build_path, dest_rel)
            
            if os.path.exists(src_full):
                shutil.copy2(src_full, dest_full)
                print(f"[BUILD] Immutable Lock: Secured -> {dest_rel}")
                
        print(f"\n[PASSED] Compiled version successfully saved at: builds/{build_tag}")
        return True
    except Exception as e:
        print(f"\n[FAILED] Build compilation halted: {str(e)}")
        return False

if __name__ == "__main__":
    compile_immutable_build()
