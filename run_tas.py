# Author: Garyoung Gary Lee, Alexis Yang

import argparse
from TAS import tas

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', required=True, help='path of input fragment matrix (fragment size X distance)')
    parser.add_argument('-pe', '--promoter_or_enhancer', choices=['enhancer', 'promoter'], 
                        required=True, help='Specify your ROI is promoter or enhancer')
    parser.add_argument('-m', "--mode", help='Specify pfTAS if you want to position free mode', choices=['TAS', 'pfTAS'], default='TAS')
    parser.add_argument('-a', "--agg", default='false', choices=['True', 'true', 'False', 'false'], 
                        help='Let it know if your input is already aggregated (in the case you are running pfTAS mode)')

    args = parser.parse_args()
    
    _p_input = args.input
    _p_pe = args.promoter_or_enhancer
    _p_mode = args.mode
    _p_agg = args.agg
    if _p_agg.lower() =='true':
        _p_agg =  True
    elif _p_agg.lower() =='false':
        _p_agg =  False
        
    result = tas.get_tas(_p_input, _p_pe, _p_mode, _p_agg)
    output = '{roi} {mode} : {output}'
    print(output.format(roi=_p_pe, mode=_p_mode, output=result))
    return result
if __name__ == "__main__":
    main()