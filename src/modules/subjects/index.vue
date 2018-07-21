<template>
  <SubjectList :courses="subjects" />
</template>

<script>
import { mapGetters } from 'vuex'
import store from './_store'
import SubjectList from './_components/SubjectList'

export default {
  name: 'SubjectModule',
  components: {
    SubjectList
  },
  computed: {
    ...mapGetters({
      subjects: '$_subjects/subjects'
    }),
    course () {
      // We will see what `params` is shortly
      return this.$route.params.courseId
    }
  },
  created () {
    const STORE_KEY = '$_subjects'
    // eslint-disable-next-line no-underscore-dangle
    if (!(STORE_KEY in this.$store._modules.root._children)) {
      this.$store.registerModule(STORE_KEY, store)
    }
  },
  mounted () {
    this.$store.dispatch('$_subjects/getSubjects', this.course)
  }
}
</script>
