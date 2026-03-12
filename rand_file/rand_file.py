# Author: phuchduong
# GitHub: https://github.com/phuchduong
# Date: March 11, 2026

import random
import subprocess
from pathlib import Path

class RandFile:
    """
    A utility to recursively scan a directory for video files and 
    launch a random selection in a specified media player.
    """

    def __init__(self, base_dir, program):
        """
        Initializes the RandFile instance, builds the file cache, and triggers an initial selection.
        
        Args:
            base_dir (str/Path): The root directory to start scanning.
            program (str): The executable path for the media player.
        """
        self.base_dir = Path(base_dir)
        self.program = program
        self.file_list = []

        print("Building file list...")
        self.rbuild_file_list(self.base_dir)
        print(f"File list complete. {len(self.file_list)} files found.")

        if self.file_list:
            self.re_roll()
        else:
            print("No video files found in the specified directory.")

    def re_roll(self):
        """
        Selects a random file from the internal list, launches it in the 
        configured player, and highlights the file in Windows Explorer.
        """
        if not self.file_list:
            return

        print("Picking a random file...")
        chosen_relative_path = random.choice(self.file_list)
        
        # Resolve to a fully qualified absolute path to avoid ambiguity
        full_path = (self.base_dir / chosen_relative_path).resolve()
        
        print(f"Playing: {full_path}")

        # Launch the media player as a background process
        subprocess.Popen([self.program, str(full_path)])

        # Open Windows Explorer and highlight the specific file
        # Passing arguments as a list ensures spaces in filenames are handled correctly
        subprocess.run(['explorer.exe', '/select,', str(full_path)])

    def rbuild_file_list(self, current_dir):
        """
        Recursively traverses the directory tree to identify video files.
        Checks for Windows MAX_PATH limitations during discovery.
        
        Args:
            current_dir (Path): The current directory level being scanned.
        """
        # Standard Windows API limit for path strings
        MAX_PATH_LENGTH = 260 

        for path in current_dir.rglob('*'):
            if path.is_file() and is_video_file(path.name):
                full_path_str = str(path.resolve())
                path_len = len(full_path_str)

                # Alert the user if a file path might cause issues with Windows APIs
                if path_len > MAX_PATH_LENGTH:
                    print(f"⚠️  ALERT: Path too long ({path_len} chars): {full_path_str}")
                
                # Store paths relative to base_dir to keep the list lightweight
                self.file_list.append(path.relative_to(self.base_dir))


def is_video_file(filename):
    """
    Determines if a file is a video based on its extension.
    
    Args:
        filename (str): The name or path of the file to check.
        
    Returns:
        bool: True if the extension matches the whitelist, False otherwise.
    """
    video_extensions = (
        '.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2', '.60d', '.787', '.89', '.aaf', '.aec',
        '.aep', '.aepx', '.aet', '.aetx', '.ajp', '.ale', '.am', '.amc', '.amv', '.amx', '.anim', '.aqt', '.arcut',
        '.arf', '.asf', '.asx', '.avb', '.avc', '.avd', '.avi', '.avp', '.avs', '.avs', '.avv', '.axm', '.bdm',
        '.bdmv', '.bdt2', '.bdt3', '.bik', '.bin', '.bix', '.bmk', '.bnp', '.box', '.bs4', '.bsf', '.bvr', '.byu',
        '.camproj', '.camrec', '.camv', '.ced', '.cel', '.cine', '.cip', '.clpi', '.cmmp', '.cmmtpl', '.cmproj',
        '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v', '.d3v', '.dav', '.dce', '.dck', '.dcr', '.dcr',
        '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb', '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d', '.dmss', '.dmx',
        '.dnc', '.dpa', '.dpg', '.dream', '.dsy', '.dv', '.dv-avi', '.dv4', '.dvdmedia', '.dvr', '.dvr-ms', '.dvx',
        '.dxr', '.dzm', '.dzp', '.dzt', '.edl', '.evo', '.eye', '.ezt', '.f4p', '.f4v', '.fbr', '.fbr', '.fbz',
        '.fcp', '.fcproject', '.ffd', '.flc', '.flh', '.fli', '.flv', '.flx', '.gfp', '.gl', '.gom', '.grasp', '.gts',
        '.gvi', '.gvp', '.h264', '.hdmov', '.hkm', '.ifo', '.imovieproj', '.imovieproject', '.ircp', '.irf', '.ism',
        '.ismc', '.ismv', '.iva', '.ivf', '.ivr', '.ivs', '.izz', '.izzy', '.jss', '.jts', '.jtv', '.k3g', '.kmv',
        '.ktn', '.lrec', '.lsf', '.lsx', '.m15', '.m1pg', '.m1v', '.m21', '.m21', '.m2a', '.m2p', '.m2t', '.m2ts', '.m2v',
        '.m4e', '.m4u', '.m4v', '.m75', '.mani', '.meta', '.mgv', '.mj2', '.mjp', '.mjpg', '.mk3d', '.mkv', '.mmv', '.mnv',
        '.mob', '.mod', '.modd', '.moff', '.moi', '.moov', '.mov', '.movie', '.mp21', '.mp21', '.mp2v', '.mp4', '.mp4v',
        '.mpe', '.mpeg', '.mpeg1', '.mpeg4', '.mpf', '.mpg', '.mpg2', '.mpgindex', '.mpl', '.mpl', '.mpls', '.mpsub',
        '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse', '.msh', '.mswmm', '.mts', '.mtv', '.mvb', '.mvc', '.mvd', '.mve',
        '.mvex', '.mvp', '.mvp', '.mvy', '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut', '.nuv', '.nvc', '.ogm',
        '.ogv', '.ogx', '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi', '.photoshow', '.piv', '.pjs', '.playlist',
        '.plproj', '.pmf', '.pmv', '.pns', '.ppj', '.prel', '.pro', '.prproj', '.prtl', '.psb', '.psh', '.pssd',
        '.pva', '.pvr', '.pxv', '.qt', '.qtch', '.qtindex', '.qtl', '.qtm', '.qtz', '.r3d', '.rcd', '.rcproject',
        '.rdb', '.rec', '.rm', '.rmd', '.rmd', '.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp', '.rsx', '.rts', '.rts',
        '.rum', '.rv', '.rvid', '.rvl', '.sbk', '.sbt', '.scc', '.scm', '.scm', '.scn', '.screenflow', '.sec', '.sedprj',
        '.seq', '.sfd', '.sfvidcap', '.siv', '.smi', '.smi', '.smil', '.smk', '.sml', '.smv', '.spl', '.sqz', '.srt',
        '.ssf', '.ssm', '.stl', '.str', '.stx', '.svi', '.swf', '.swi', '.swt', '.tda3mt', '.tdx', '.thp', '.tivo',
        '.tix', '.tod', '.tp', '.tp0', '.tpd', '.tpr', '.trp', '.ts', '.tsp', '.ttxt', '.tvs', '.usf', '.usm', '.vc1',
        '.vcpf', '.vcr', '.vcv', '.vdo', '.vdr', '.vdx', '.veg', '.vem', '.vep', '.vf', '.vft', '.vfw', '.vfz', '.vgz',
        '.vid', '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob', '.vp3', '.vp6', '.vp7', '.vpj', '.vro', '.vs4',
        '.vse', '.vsp', '.w32', '.wcp', '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv', '.wmx', '.wot', '.wp3', '.wpl',
        '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl', '.xlmv', '.xmv', '.xvid', '.y4m', '.yog', '.yuv', '.zeg',
        '.zm1', '.zm2', '.zm3', '.zmv')

    return Path(filename).suffix.lower() in video_extensions
