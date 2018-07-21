  <template>
  <v-list>
   <v-list-tile v-for="item in courses" :key="item.title" :to="{path: 'subject/' + item.id}">
     <v-list-tile-action>
              <v-icon>Home</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{item.name}}</v-list-tile-title>
            </v-list-tile-content>
   </v-list-tile>
  </v-list>
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
