#parse data

class Times:
	def __init__(self):
		self.data = {}

	@staticmethod
	def get_num_spaces(input_str):
		return len(input_str) - len(input_str.lstrip())

	def fill(self, input_str):
		lines = input_str.splitlines()

		last_header = None
		depth = None 

		for i in range(len(lines)):
			if lines[i][0] is not '#':
				continue
				

			line = lines[i]
			num_spaces = get_num_spaces(line)

			if num_spaces == 0:
				header = line


				while ()





data = '''
###################################
ROUND 1
###################################

INFERENCE
  alpha: 1.409982 sec
  likelihood: 0.000001 sec
  beta: 1.991809 sec
  gamma: 0.010420 sec

  INFERENCE SUBTOTAL: 3.412239 sec

REESTIMATION
  pi: 0.000002 sec

  transition probabilities
    cjk: 0.455195 sec
    transition prob NO PARALLEL: 0.000031 sec
    fill trans: 0.037122 sec

    TRANS PROB SUBTOTAL: 0.492370 sec

  mu,phi
    calculate mu,phi
      x,y-init: 0.008411 sec
      offset-init: 0.025662 sec
      offset-adjust mapp: 0.007004 sec
      prior-load: 0.018925 sec
      prior-update: 0.539657 sec

      GLM NB
        initial fit
          initialize weights and residual: 0.012203 sec

          IRLS
            iteration 0: 0.121052 sec
            iteration 1: 0.149152 sec
            iteration 2: 0.106649 sec
            iteration 3: 0.105523 sec
            iteration 4: 0.111346 sec

            IRLS SUBTOTAL: 0.593770 sec

        test for overdispersion: 0.004919 sec
        log likelihood: 0.000001 sec
        phi_ml: 10.452874 sec
        log likelihood NB: 0.134649 sec

        iterative fits
        ITER 0
          initialize weights and residual: 0.014907 sec

          IRLS
            iteration 0: 0.107695 sec
            iteration 1: 0.107618 sec
            iteration 2: 0.107079 sec
            iteration 3: 0.147934 sec
            iteration 4: 0.121888 sec
            iteration 5: 0.122348 sec
            iteration 6: 0.126113 sec
            iteration 7: 0.132778 sec

            IRLS SUBTOTAL: 0.973531 sec

          FIT SUBTOTAL: 0.134846 sec

        ITER 1
          initialize weights and residual: 0.021746 sec

          IRLS
            iteration 0: 0.120036 sec
            iteration 1: 0.105960 sec
            iteration 2: 0.106445 sec
            iteration 3: 0.128391 sec

            IRLS SUBTOTAL: 0.460872 sec

          FIT SUBTOTAL: 0.130469 sec

        ITER 2
          initialize weights and residual: 0.015029 sec

          IRLS
            iteration 0: 0.107550 sec
            iteration 1: 0.107047 sec

            IRLS SUBTOTAL: 0.214616 sec

          FIT SUBTOTAL: 0.109124 sec

        ITER 3
          initialize weights and residual: 0.015219 sec

          IRLS
            iteration 0: 0.108661 sec
            iteration 1: 0.107307 sec

            IRLS SUBTOTAL: 0.215987 sec

          FIT SUBTOTAL: 0.109398 sec

        ITER 4
          initialize weights and residual: 0.014960 sec

          IRLS
            iteration 0: 0.109302 sec
            iteration 1: 0.108360 sec

            IRLS SUBTOTAL: 0.217682 sec

          FIT SUBTOTAL: 0.110456 sec

        ITER 5
          initialize weights and residual: 0.014984 sec

          IRLS
            iteration 0: 0.126470 sec
            iteration 1: 0.120414 sec

            IRLS SUBTOTAL: 0.246905 sec

          FIT SUBTOTAL: 0.122532 sec

        ITER 6
          initialize weights and residual: 0.015029 sec

          IRLS
            iteration 0: 0.122574 sec
            iteration 1: 0.127095 sec

            IRLS SUBTOTAL: 0.249688 sec

          FIT SUBTOTAL: 0.129239 sec

        ITER 7
          initialize weights and residual: 0.015578 sec

          IRLS
            iteration 0: 0.138562 sec
            iteration 1: 0.106961 sec

            IRLS SUBTOTAL: 0.245543 sec

          FIT SUBTOTAL: 0.109132 sec

        ITER 8
          initialize weights and residual: 0.016535 sec

          IRLS
            iteration 0: 0.114660 sec
            iteration 1: 0.111296 sec

            IRLS SUBTOTAL: 0.225976 sec

          FIT SUBTOTAL: 0.113631 sec

        ITER 9
          initialize weights and residual: 0.015125 sec

          IRLS
            iteration 0: 0.109379 sec
            iteration 1: 0.107069 sec

            IRLS SUBTOTAL: 0.216468 sec

          FIT SUBTOTAL: 0.109243 sec

        ITER 10
          initialize weights and residual: 0.015693 sec

          IRLS
            iteration 0: 0.107831 sec
            iteration 1: 0.106180 sec

            IRLS SUBTOTAL: 0.214029 sec

          FIT SUBTOTAL: 0.108323 sec

        GLM NB SUBTOTAL: 22.966162 sec

			beta for gc content is 0.695429
      mu-save fitted: 0.006940 sec
      phi_ml: 10.576307 sec

      MU,PHI SUBTOTAL: 34.165156 sec

    calculate mu,phi (AR)
      x,y-init: 0.062892 sec
      offset-init: 0.025700 sec
      offset-adjust mapp: 0.007044 sec
      prior-load: 0.018821 sec
      prior-update: 0.567144 sec

      fitting glm NB
        initial fit
          initialize weights and residual: 0.012110 sec

          IRLS
            iteration 0: 0.182962 sec
            iteration 1: 0.156477 sec
            iteration 2: 0.152235 sec
            iteration 3: 0.151740 sec
            iteration 4: 0.166237 sec

            IRLS SUBTOTAL: 0.809701 sec

        test for overdispersion: 0.004169 sec
        log likelihood: 0.000000 sec
        phi_ml: 10.914647 sec
        log likelihood NB: 0.148646 sec

        iterative fits
        ITER 0
          initialize weights and residual: 0.015197 sec

          IRLS
            iteration 0: 0.154552 sec
            iteration 1: 0.154753 sec
            iteration 2: 0.179142 sec
            iteration 3: 0.171320 sec
            iteration 4: 0.152623 sec
            iteration 5: 0.163321 sec
            iteration 6: 0.158286 sec

            IRLS SUBTOTAL: 1.134063 sec

          FIT SUBTOTAL: 0.160421 sec

        ITER 1
          initialize weights and residual: 0.015189 sec

          IRLS
            iteration 0: 0.155154 sec
            iteration 1: 0.158756 sec
            iteration 2: 0.157806 sec
            iteration 3: 0.152709 sec
            iteration 4: 0.152820 sec

            IRLS SUBTOTAL: 0.777293 sec

          FIT SUBTOTAL: 0.154956 sec

        ITER 2
          initialize weights and residual: 0.015073 sec

          IRLS
            iteration 0: 0.160189 sec
            iteration 1: 0.189495 sec

            IRLS SUBTOTAL: 0.349703 sec

          FIT SUBTOTAL: 0.191799 sec

        ITER 3
          initialize weights and residual: 0.015062 sec

          IRLS
            iteration 0: 0.175754 sec
            iteration 1: 0.153706 sec

            IRLS SUBTOTAL: 0.329478 sec

          FIT SUBTOTAL: 0.155837 sec

        ITER 4
          initialize weights and residual: 0.014881 sec

          IRLS
            iteration 0: 0.154246 sec
            iteration 1: 0.152937 sec

            IRLS SUBTOTAL: 0.307200 sec

          FIT SUBTOTAL: 0.155093 sec

        ITER 5
          initialize weights and residual: 0.015063 sec

          IRLS
            iteration 0: 0.154093 sec
            iteration 1: 0.153586 sec

            IRLS SUBTOTAL: 0.307696 sec

          FIT SUBTOTAL: 0.155695 sec

        ITER 6
          initialize weights and residual: 0.017262 sec

          IRLS
            iteration 0: 0.168307 sec
            iteration 1: 0.153233 sec

            IRLS SUBTOTAL: 0.321559 sec

          FIT SUBTOTAL: 0.155362 sec

        ITER 7
          initialize weights and residual: 0.015010 sec

          IRLS
            iteration 0: 0.169550 sec
            iteration 1: 0.152871 sec

            IRLS SUBTOTAL: 0.322439 sec

          FIT SUBTOTAL: 0.154982 sec

        ITER 8
          initialize weights and residual: 0.018177 sec

          IRLS
            iteration 0: 0.171501 sec
            iteration 1: 0.156612 sec

            IRLS SUBTOTAL: 0.328132 sec

          FIT SUBTOTAL: 0.158753 sec

        ITER 9
          initialize weights and residual: 0.017960 sec

          IRLS
            iteration 0: 0.184220 sec
            iteration 1: 0.172157 sec

            IRLS SUBTOTAL: 0.356396 sec

          FIT SUBTOTAL: 0.174284 sec

        ITER 10
          initialize weights and residual: 0.015020 sec

          IRLS
            iteration 0: 0.193604 sec
            iteration 1: 0.166340 sec

            IRLS SUBTOTAL: 0.359963 sec

          FIT SUBTOTAL: 0.168541 sec

      fitting glm NB SUBTOTAL: 25.445286 sec
		beta for gc content is 0.642608 
		mu adjusted for state 0
      mu-adjust: 0.009728 sec
      phi: 11.013596 sec

      MU,PHI (AR) SUBTOTAL: 37.171667 sec

  fill emission table: 0.600645 sec

  REESTIMATION SUBTOTAL: 72.429954 sec

ROUND TOTAL: 75.842193 sec
'''

mydata = Times()
mydata.fill(data)