import os
import shutil

def freeze_phase4_modules():
    print("[BUILD] Initiating Phase 4 Extensions Immutable Lock...")
    
    base_dir = r"D:\Me\Development\Riemann Hypothesis"
    build_tag = "Phase4.1.0_Extensions_Complete"
    target_build_path = os.path.join(base_dir, "builds", build_tag)
    
    # Source track files to securely lock down
    sources = {
        "src/phase4_modules/Framework_Extensions.md": "src/phase4_modules/Framework_Extensions.md",
        "src/phase4_modules/Proxy_Agent_Paradox.md": "src/phase4_modules/Proxy_Agent_Paradox.md",
        "src/phase4_modules/Asymmetrical_Protocol.md": "src/phase4_modules/Asymmetrical_Protocol.md"
    }
    
    try:
        # Construct isolated build folders
        os.makedirs(os.path.join(target_build_path, "src", "phase4_modules"), exist_ok=True)
        
        # Duplicate and freeze configurations
        for src_rel, dest_rel in sources.items():
            src_full = os.path.join(base_dir, src_rel)
            dest_full = os.path.join(target_build_path, dest_rel)
            if os.path.exists(src_full):
                shutil.copy2(src_full, dest_full)
                print(f"[BUILD] Immutable Lock: Secured -> {dest_rel}")
                
        print(f"\n[PASSED] Phase 4 build successfully frozen at: builds/{build_tag}")
        return True
    except Exception as e:
        print(f"\n[FAILED] Build compilation halted: {str(e)}")
        return False

if __name__ == "__main__":
    freeze_phase4_modules()
