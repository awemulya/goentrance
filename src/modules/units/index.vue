<template>
  <UnitList :units="units" />
</template>

<script>
import { mapGetters } from 'vuex'
import store from './_store'
import UnitList from './_components/UnitList'

export default {
  name: 'UnitModule',
  components: {
    UnitList
  },
  computed: {
    ...mapGetters({
      units: '$_units/units'
    }),
    subject () {
      // We will see what `params` is shortly
      return this.$route.params.subjectId
    }
  },
  created () {
    const STORE_KEY = '$_units'
    // eslint-disable-next-line no-underscore-dangle
    if (!(STORE_KEY in this.$store._modules.root._children)) {
      this.$store.registerModule(STORE_KEY, store)
    }
  },
  mounted () {
    this.$store.dispatch('$_units/getUnits', this.subject)
  }
}
</script>
