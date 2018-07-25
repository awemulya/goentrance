  <template>
  <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <v-card>
          <v-toolbar color="teal" dark>
            <v-toolbar-side-icon></v-toolbar-side-icon>
            <v-toolbar-title class="text-xs-center">Courses</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon>
              <v-icon>search</v-icon>
            </v-btn>
          </v-toolbar>
          <v-list subheader>
            <v-subheader>Availabale Courses</v-subheader>
            <v-list-tile
              v-for="item in courses"
              :key="item.id"
              avatar
              :to="{path: 'subject/' + item.id}"
            >
              <v-list-tile-avatar>
                <img src="@/assets/courses.png" alt="">
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title v-html="item.name"></v-list-tile-title>
              </v-list-tile-content>
              <v-list-tile-action>
                <v-icon :color="item.id ? 'teal' : 'grey'">notifications</v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
          <v-divider></v-divider>
          <v-list subheader>
            <v-subheader>Recent Courses</v-subheader>
            <v-list-tile
              v-for="item in courses"
              :key="item.id"
              avatar
             :to="{path: 'subject/' + item.id}"
            >
              <v-list-tile-avatar>
                <img src="@/assets/logo.png" alt="">
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title v-html="item.name"></v-list-tile-title>
              </v-list-tile-content>
               <v-list-tile-action>
                <v-icon :color="item.id ? 'teal' : 'grey'">email</v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
  </template>

<script>
import { mapGetters } from 'vuex'
import store from './_store'
import CourseList from './_components/CourseList'

export default {
  name: 'CourseModule',
  components: {
    CourseList
  },
  computed: {
    ...mapGetters({
      courses: '$_courses/courses'
    })
  },
  created () {
    const STORE_KEY = '$_courses'
    // eslint-disable-next-line no-underscore-dangle
    if (!(STORE_KEY in this.$store._modules.root._children)) {
      this.$store.registerModule(STORE_KEY, store)
    }
  },
  mounted () {
    this.$store.dispatch('$_courses/getCourses')
  },
  props: {
    source: String
  }
}
</script>
