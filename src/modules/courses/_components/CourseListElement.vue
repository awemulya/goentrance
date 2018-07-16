<template>
  <tr>
    <td v-text="product.name"></td>
  </tr>
</template>

<script>
export default {
  name: 'CoursetListElement',
  props: {
    product: {
      type: Object
    }
  }
}
</script>
