import random
import os
import subprocess


class rand_file:

    def __init__(self, base_dir, program):
        self.base_dir = base_dir
        self.file_list = []
        self.program = program

        print("Building file list...")
        self.rbuild_file_list(self.base_dir)
        print("File list complete...")

        self.print_list()
        print(str(len(self.file_list)) + " files in list...")

        self.re_roll()

    def re_roll(self):
        print("Picking a random file from the list...")
        rand_file_str = random.choice(self.file_list)
        rand_file = rand_file_str.encode('utf-8')
        print(rand_file)
        # Opens the file
        file_path = self.base_dir + rand_file_str
        subprocess.Popen([self.program, file_path])

        parent_folder = os.path.dirname(file_path)
        os.startfile(parent_folder)

    def rbuild_file_list(self, current_dir):
        dir_list = os.listdir(current_dir)
        for dir_name in dir_list:
            file_root = current_dir + "\\" + dir_name
            if os.path.isfile(file_root):
                if is_video_file(dir_name):
                    # asbsolute to relative pathing
                    relative_file_path = file_root.replace(self.base_dir, "")
                    self.file_list.append(relative_file_path)
            elif os.path.isdir(file_root):
                self.rbuild_file_list(file_root)
            else:
                print("Invalid file state: " + str(file_root))

    def print_list(self):
        for item in self.file_list:
            print(str(item))


def is_video_file(filename):
    video_file_extensions = (
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

    if filename.lower().endswith((video_file_extensions)):
        return True
