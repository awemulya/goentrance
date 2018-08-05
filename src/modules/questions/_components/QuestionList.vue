  <template>
  <v-layout row>
      <v-flex  xs12 sm6 offset-sm3>
        <v-card>
          <v-card-media
            v-bind:src="background"
            height="300px"
          >
          </v-card-media>
          <v-card-title primary-title>
            <div>
              <div class="headline">Questions {{questions.length}} {{set}}</div>
              <span class="grey--text">Time 1 min</span>
            </div>
          </v-card-title>
          <v-card-actions>
           <v-btn @click="countdown" v-if="!end">
            <countdown v-if="counting" :time="time" :leading-zero="false" :emit-events=true @countdownend="countdownend"  ref="countdown">
              <template slot-scope="props">Time Remaining{{ props.hours }} hours, {{ props.minutes }} minutes,  {{ props.totalSeconds }} seconds </template>
            </countdown>
            <span v-else>Start Entrance</span>
           </v-btn>
           <v-btn v-if="end">
              <span>Time Taken :{{timetaken}}</span>
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
          <v-toolbar color="pink" dark>
            <v-toolbar-side-icon></v-toolbar-side-icon>
            <v-toolbar-title>Results</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon>
              <v-icon>search</v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>check_circle</v-icon>
            </v-btn>
          </v-toolbar>
          <v-list two-line>
            <template v-for="(item, index) in items">
              <v-list-tile :key="index" avatar ripple >
                <v-list-tile-content>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                  <v-list-tile-sub-title class="text--primary">{{ item.headline }}</v-list-tile-sub-title>
                  <v-list-tile-sub-title>{{ item.subtitle }}</v-list-tile-sub-title>
                </v-list-tile-content>
                <v-list-tile-action>
                  <v-list-tile-action-text>{{ item.action }}</v-list-tile-action-text>
                  <v-icon color="grey lighten-1">star_border</v-icon>
                </v-list-tile-action>
              </v-list-tile>
              <v-divider v-if="index + 1 < items.length" :key="`divider-${index}`"></v-divider>
            </template>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
  </template>

<script>
import VueCountdown from '@xkeshi/vue-countdown'

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
    question_no: 0,
    counting: false,
    time: 5000,
    items: [
      { action: '15 min', headline: 'Brunch this weekend?', title: 'Ali Connors', subtitle: "I'll be in your neighborhood doing errands this weekend. Do you want to hang out?" },
      { action: '2 hr', headline: 'Summer BBQ', title: 'me, Scrott, Jennifer', subtitle: "Wish I could come, but I'm out of town this weekend." },
      { action: '6 hr', headline: 'Oui oui', title: 'Sandra Adams', subtitle: 'Do you have Paris recommendations? Have you ever been?' },
      { action: '12 hr', headline: 'Birthday gift', title: 'Trevor Hansen', subtitle: 'Have any ideas about what we should get Heidi for her birthday?' },
      { action: '18hr', headline: 'Recipe to try', title: 'Britta Holt', subtitle: 'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.' }
    ]
  }),
  components: {
    'countdown': VueCountdown
  },
  props: {
    questions: {
      type: Array
    },
    set: {
      type: Object
    }
  },
  computed: {
    background () {
      return require('@/assets/yatra.jpg')
    },
    timetaken () {
      var taken = this.time - this.$refs.countdown.count
      return this.msToHMS(taken)
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
        this.$refs.countdown.pause()
      }
    },
    countdown: function () {
      this.counting = true
      this.start = true
    },
    countdownend: function () {
      this.$refs.countdown.pause()
      this.end = true
    },
    msToHMS (ms) {
      var seconds = ms / 1000
      var hours = parseInt(seconds / 3600) // 3,600 seconds in 1 hour
      seconds = seconds % 3600 // seconds remaining after extracting hours
      var minutes = parseInt(seconds / 60) // 60 seconds in 1 minute
      seconds = seconds % 60
      return (hours + ' Hours, ' + minutes + ' Minutes, ' + seconds + ' Seconds')
    }
  },
  watch: {
    // whenever start changes, this function will run
    start: function (newValue, oldValue) {
      this.question = this.questions[this.question_no]
    },
    time: function (newValue, oldValue) {
      console.log(newValue)
    }
  }
}
</script>

<style scoped>

</style>
