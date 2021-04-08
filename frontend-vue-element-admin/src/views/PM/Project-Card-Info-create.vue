<template>
  <project-detail :is-edit="false" />
</template>

<script>
import ProjectDetail from './components/ProjectDetail'

export default {
  name: 'CreateForm',
  components: { ProjectDetail }
}
</script>

