MPG = 48.00
PER100 = 100

START_POS = 1
END_POS = 5

BIPM_POS_STATS = ['pts', 'tpg', 'ast', 'tov', 'orb', 'drb', 'stl', 'blk', 'pf']
BIPM_ROLE_STATS = ['fga', 'fta']

# BIPM Position Coefficients
BIPM_PTS = (0.860,None)
BIPM_3PM = (0.389,None)
BIPM_AST = (0.580,1.034)
BIPM_TO = (-0.964,None)
BIPM_ORB = (0.613,0.181)
BIPM_DRB = (0.116, 0.181)
BIPM_STL = (1.369, 1.008)
BIPM_BLK = (1.327,0.703)
BIPM_PF = (-0.367,None)

# BIPM Role Coefficients
BIPM_FGA = (-0.560,-0.780)
BIPM_FTA = (-0.246,-0.343)