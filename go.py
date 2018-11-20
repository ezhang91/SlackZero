import os
import sys

DIR=os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(DIR, 'deps'))

import djangogo

parser=djangogo.make_parser()
args=parser.parse_args()
djangogo.main(args,
	project='SlackZero_proj',
	app='SlackZero',
	database='SlackZero_database',
	user='SlackZero_user',
	heroku_url='https://sheltered-sands-95126.herokuapp.com/',
)
