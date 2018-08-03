  <template>
  <v-layout row>
      <v-flex  xs12 sm6 offset-sm3>
        <v-card v-show="!start">
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
        <v-card v-show="start">
          <v-card-text>
        <v-container fluid>
          <v-layout row wrap>
            <v-flex xs12>
              <v-radio-group v-model="color" row>
                <v-radio
                  v-for="(colorValue, i) in ['success', 'info', 'error', 'cyan darken-2']"
                  :color="colorValue"
                  :key="i"
                  :label="colorValue"
                  :value="colorValue"
                ></v-radio>
              </v-radio-group>
            </v-flex>
            <v-flex xs12 sm3>
              <v-checkbox
                v-model="mode"
                label="Multi-line (mobile)"
                value="multi-line"
              ></v-checkbox>
            </v-flex>
            <v-flex xs12 sm3>
              <v-checkbox
                v-model="mode"
                label="Vertical (mobile)"
                value="vertical"
              ></v-checkbox>
            </v-flex>
            <v-flex xs12 sm4 offset-sm4>
              <v-text-field
                v-model="text"
                label="Text"
                type="text"
              ></v-text-field>
            </v-flex>
            <v-flex xs12 sm4>
              <v-text-field
                v-model.number="timeout"
                label="Timeout"
                type="number"
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>
        <v-btn
          block
          color="primary"
          dark
          @click="snackbar = true"
        >
          Show Snackbar
        </v-btn>
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
      </v-flex>
    </v-layout>
  </template>

<script>

export default {
  name: 'QuestionList',
  data: () => ({
    start: false,
    show: false,
    snackbar: false,
    color: '',
    mode: '',
    timeout: 6000,
    text: 'Hello, I\'m a snackbar'
  }),
  components: {
  },
  props: {
    questions: {
      type: Array
    }
  },
  watch: {
    // whenever start changes, this function will run
    start: function (newValue, oldValue) {
      console.log(newValue)
    }
  }
}
</script>

<style scoped>

</style>
