#parse data
from itertools import izip

directory = '/home/bentzou/Code/parallel-genseng/data_orig/'
file_no_omp = 'output-no-omp'
file_omp = 'output-omp'


class Times:
  def __init__(self):
    self.data = {}

  @staticmethod
  def get_num_spaces(input_str):
    return len(input_str) - len(input_str.lstrip())

  @staticmethod
  def get_num_indents(input_str, spaces_per_indent=2):
    return get_num_spaces(input_str) / spaces_per_indent

  @staticmethod
  def parse(filename):
    alphas = []
    betas = []
    likelihoods = []
    gammas = []
    inference_totals = []

    pis = []
    cjks = []
    fill_trans = []
    trans_probs_totals = []

    mu_phi_xy = []
    mu_phi_offset_init = []
    mu_phi_offset_adjust = []
    mu_phi_prior_load = []
    mu_phi_prior_update = []

    init_weights = []
    iteration = []
    test_for_overdispersion = []
    log_likelihood = []
    phi_ml = []
    log_likelihood_nb = []
    glm_nb_subtotal = []

    mu_save_fitted = []
    mu_phi_subtotal = []
    fitting_glm_nb_subtotal = []
    mu_adjust = []
    mu_phi_ar_subtotal = []

    fill_emission_table = []
    reestimation_subtotal = []

    round_total = []
    total_time = None

    with open(filename) as infile:
      for line in infile:
        temp = line.strip()

        if temp == None:
          continue
        elif temp.startswith('alpha:'):
          alphas.append(temp.split()[1])
        elif temp.startswith('likelihood:'):
          likelihoods.append(temp.split()[1])
        elif temp.startswith('beta:'):
          betas.append(temp.split()[1])
        elif temp.startswith('gamma:'):
          gammas.append(temp.split()[1])
        elif temp.startswith('INFERENCE SUBTOTAL:'):
          inference_totals.append(temp.split()[2])

        elif temp.startswith('pi:'):
          pis.append(temp.split()[1])
        elif temp.startswith('cjk:'):
          cjks.append(temp.split()[1])
        elif temp.startswith('fill trans:'):
          fill_trans.append(temp.split()[2])
        elif temp.startswith('TRANS PROB SUBTOTAL:'):
          trans_probs_totals.append(temp.split()[3])

        elif temp.startswith('x,y-init:'):
          mu_phi_xy.append(temp.split()[1])
        elif temp.startswith('offset-init:'):
          mu_phi_offset_init.append(temp.split()[1])
        elif temp.startswith('offset-adjust mapp:'):
          mu_phi_offset_adjust.append(temp.split()[2])
        elif temp.startswith('prior-load:'):
          mu_phi_prior_load.append(temp.split()[1])
        elif temp.startswith('prior-update:'):
          mu_phi_prior_update.append(temp.split()[1])

        elif temp.startswith('initialize weights and residual:'):
          init_weights.append(temp.split()[4])
        elif temp.startswith('iteration '):
          iteration.append(temp.split()[2])
        elif temp.startswith('test for overdispersion:'):
          test_for_overdispersion.append(temp.split()[3])
        elif temp.startswith('log likelihood:'):
          log_likelihood.append(temp.split()[2])
        elif temp.startswith('phi_ml:') or temp.startswith('phi:'):
          phi_ml.append(temp.split()[1])
        elif temp.startswith('log likelihood NB:'):
          log_likelihood_nb.append(temp.split()[3])
        elif temp.startswith('GLM NB SUBTOTAL:'):
          glm_nb_subtotal.append(temp.split()[3])

        elif temp.startswith('mu-save fitted:'):
          mu_save_fitted.append(temp.split()[2])
        elif temp.startswith('MU,PHI SUBTOTAL:'):
          mu_phi_subtotal.append(temp.split()[2])

        elif temp.startswith('fitting glm NB SUBTOTAL:'):
          fitting_glm_nb_subtotal.append(temp.split()[4])
        elif temp.startswith('mu-adjust:'):
          mu_adjust.append(temp.split()[1])
        elif temp.startswith('MU,PHI (AR) SUBTOTAL:'):
          mu_phi_ar_subtotal.append(temp.split()[3])

        elif temp.startswith('fill emission table:'):
          fill_emission_table.append(temp.split()[3])
        elif temp.startswith('REESTIMATION SUBTOTAL:'):
          reestimation_subtotal.append(temp.split()[2])
        elif temp.startswith('ROUND TOTAL:'):
          round_total.append(temp.split()[2])

        elif temp.startswith('INFER AND ESTIMATION TOTAL TIME:'):
          total_time = temp.split()[5]


    variables = '''alphas, betas, likelihoods, gammas, inference_totals,
      pis, cjks, fill_trans, trans_probs_totals,

      mu_phi_xy, mu_phi_offset_init, mu_phi_offset_adjust,
      mu_phi_prior_load, mu_phi_prior_update,

      init_weights, iteration, test_for_overdispersion, log_likelihood,
      phi_ml, log_likelihood_nb, glm_nb_subtotal,

      mu_save_fitted, mu_phi_subtotal, fitting_glm_nb_subtotal,
      mu_adjust, mu_phi_ar_subtotal,

      fill_emission_table, reestimation_subtotal, round_total

      '''

    variable_names = [variable.strip() for variable in variables.split(',')]

    for variable in variable_names:
      lst = [float(item) for item in eval(variable) if float(item)]

      lst.sort()
      newlist = lst[1:len(lst)-1]

      total = sum(newlist)
      num = len(newlist)
      avg = total / num

      print len(eval(variable)), variable + ':', avg

    print 'total time:',total_time



mydata = Times()
mydata.parse(directory + file_omp)
mydata.parse(directory + file_no_omp)



omp = '''
alphas: 1.52954175
betas: 1.902639
likelihoods: 1.125e-06
gammas: 0.01043225
inference_totals: 3.451583625
pis: 2e-06
cjks: 0.44293325
fill_trans: 0.038360625
trans_probs_totals: 0.48159425
mu_phi_xy: 0.0371542777778
mu_phi_offset_init: 0.0256263888889
mu_phi_offset_adjust: 0.007022
mu_phi_prior_load: 0.0190421666667
mu_phi_prior_update: 0.574733888889
init_weights: 0.0156004292929
iteration: 0.141988073741
test_for_overdispersion: 0.00422994444444
log_likelihood: 1e-06
phi_ml: 12.6786003684
log_likelihood_nb: 0.138426388889
glm_nb_subtotal: 21.991345
mu_save_fitted: 0.006951125
mu_phi_subtotal: 34.786000125
fitting_glm_nb_subtotal: 27.343981625
mu_adjust: 0.009753
mu_phi_ar_subtotal: 41.109652
fill_emission_table: 0.579097125
reestimation_subtotal: 78.327125625
round_total: 81.761272125
total time: 1048.111273
'''

no_omp = '''
alphas: 2.008762625
betas: 3.069442375
likelihoods: 1e-06
gammas: 0.0106395
inference_totals: 5.08724125
pis: 1.875e-06
cjks: 1.836762625
fill_trans: 0.044687125
trans_probs_totals: 1.881456875
mu_phi_xy: 0.156519777778
mu_phi_offset_init: 0.142600277778
mu_phi_offset_adjust: 0.00703277777778
mu_phi_prior_load: 0.0881194444444
mu_phi_prior_update: 1.13408116667
init_weights: 0.0400562334802
iteration: 0.370114137705
test_for_overdispersion: 0.0131428888889
log_likelihood: 1e-06
phi_ml: 62.1187901842
log_likelihood_nb: 0.673880222222
glm_nb_subtotal: 95.881458875
mu_save_fitted: 0.0070735
mu_phi_subtotal: 157.529483
fitting_glm_nb_subtotal: 132.5756235
mu_adjust: 0.010205875
mu_phi_ar_subtotal: 197.610105125
fill_emission_table: 1.14406825
reestimation_subtotal: 359.7290445
round_total: 364.8194615
total time: 3883.677177'''

# print '#'*58
# print '%25s %10s %10s %10s' % ('Parallelized Section', 'no OMP', 'OMP', 'Speedup')
# print '#'*58
# for line1,line2 in izip(omp.split('\n'), no_omp.split('\n')):
#   if not line1:
#     continue
#   name = line1.split(':')[0]
#   omp = float(line1.split(':')[1])
#   noomp = float(line2.split(':')[1])

#   if noomp < 0.001 or omp < 0.0001:
#     improvement = '--'
#   else:
#     improvement = str(noomp/omp)[:5]

#   print '%25s %10.2f %10.2f %10s' % (name, noomp, omp, improvement)
