  <template>
  <v-layout row>
      <v-flex  xs12 sm6 offset-sm3>
        <v-card v-show="!start && !end">
          <v-card-media
            src="https://cdn.vuetifyjs.com/images/cards/road.jpg"
            height="300px"
          >
          </v-card-media>
          <v-card-title primary-title>
            <div>
              <div class="headline">Questions {{questions.length}}</div>
              <span class="grey--text">Time 1 min</span>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn flat @click="start =true" v-if="start==false">
            Start
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn icon @click="show = !show">
              <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
            </v-btn>
          </v-card-actions>
          <v-slide-y-transition>
            <v-card-text v-show="show">
              Start Your Skills Test ..
            </v-card-text>
          </v-slide-y-transition>
        </v-card>
        <v-card v-show="start && !end">
          <v-card-text>
        <v-container fluid>
          <v-layout row wrap>
            <v-flex xs12>
              <v-card>
              <v-card-text>
              {{question.question}}
            </v-card-text>
              </v-card>
            </v-flex>
              <v-flex xs12>
              <v-radio-group v-model="color" column>
                <v-radio
                  v-for="option in question.options"
                  :key="option.id"
                  :label="option.answer"
                  :value="option.id"
                  @click="selected(option.id)"
                ></v-radio>
              </v-radio-group>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-snackbar
        v-model="snackbar"
        :color="color"
        :multi-line="mode === 'multi-line'"
        :timeout="timeout"
        :vertical="mode === 'vertical'"
      >
        {{ text }}
        <v-btn
          dark
          flat
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </v-snackbar>
        </v-card>
        <v-card v-show="end">
          Results
        </v-card>
      </v-flex>
    </v-layout>
  </template>

<script>

export default {
  name: 'QuestionList',
  data: () => ({
    start: false,
    end: false,
    show: false,
    snackbar: false,
    color: 'success',
    mode: '',
    timeout: 1000,
    text: 'Answer Submitted',
    question: '',
    question_no: 0
  }),
  components: {
  },
  props: {
    questions: {
      type: Array
    }
  },
  methods: {
    selected: function (value) {
      console.log(value)
      // Submit answer to question
      this.snackbar = true
      this.question_no += 1
      if (this.questions.length > this.question_no) {
        this.question = this.questions[this.question_no]
      } else {
        console.log('exam completed')
        this.end = true
      }
    }
  },
  watch: {
    // whenever start changes, this function will run
    start: function (newValue, oldValue) {
      this.question = this.questions[this.question_no]
    },
    snackbar: function (newValue, oldValue) {
      console.log(newValue)
    }
  }
}
</script>

<style scoped>

</style>
