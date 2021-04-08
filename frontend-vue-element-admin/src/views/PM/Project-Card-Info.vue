<template>
  <div class="app-container">
    <!--search bar-->
    <div class="filter-container">
      <el-tag align="right" style="margin-right: 30px" type="danger">单位：MRMB, M2</el-tag>
      <el-select v-model="listQuery.Project_name" placeholder="Name" style="width: 90px" class="filter-item">
        <el-option v-for="item in leaderOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <!--      <el-input v-model="listQuery.Project_name" placeholder="Name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />-->
      <el-select v-model="listQuery.Project_leader" placeholder="IPL" clearable style="width: 90px" class="filter-item">
        <el-option v-for="item in leaderOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.Current_status" placeholder="Stage" clearable style="width: 90px" class="filter-item">
        <el-option v-for="item in statusOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.ordering" style="width: 140px" class="filter-item" @change="handleFilter">
        <el-option v-for="item in orderingOptions" :key="item.key" :label="item.label" :value="item.key" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" style="margin-left: 30px" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <router-link :to="'/PM/Project-Card-Info/create/'" style="margin-right: 10px;margin-left: 10px;">
        <el-button class="filter-item" type="primary" icon="el-icon-edit">
          Add
        </el-button>
      </router-link>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        Export
      </el-button>
      <el-checkbox v-model="showKPI" class="filter-item" style="margin-left:15px;" @change="tableKey=tableKey+1">
        Actual KPI
      </el-checkbox>
      <el-checkbox v-model="showSchedule" class="filter-item" style="margin-left:5px;" @change="tableKey=tableKey+1">
        Actual Schedule
      </el-checkbox>
      <el-checkbox v-model="showRiskAction" class="filter-item" style="margin-left:5px;" @change="tableKey=tableKey+1">
        Risk & Action
      </el-checkbox>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @ordering-change="orderingChange"
    >
      <el-table-column label="ID" prop="id" orderingable="custom" align="center" width="40" :class-name="getorderingClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Region" width="110px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Region }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Name" min-width="100px">
        <template slot-scope="{row}">
          <span>{{ row.Project_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Leader" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Project_leader }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Stage" width="100" align="center">
        <template slot-scope="{row}">
          <el-tag :type="row.Current_status | statusFilter">
            {{ row.Current_status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="Summary" align="center" min-width="120px" :class-name="getorderingClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.Summary }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Update" min-width="100px">
        <template slot-scope="{row}">
          <span>{{ row.Update }}</span>
        </template>
      </el-table-column>
      <el-table-column v-if="showKPI" label="Actual KPI" width="80px" align="center">
        <el-table-column label="COGS" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Additional_COGS }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Prod" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Productivity }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Capex" align="center">
          <template slot-scope="{row}">
            <span>{{ row.CAPEX }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Space" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Space_needed }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Y+3 QTY" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Y_3_QTY }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Expense" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Expense }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Payback" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Payback }}</span>
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column v-if="showSchedule" label="Actual Schedule" align="center">
        <el-table-column label="Open" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Open_date }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Do" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Do_date }}</span>
          </template>
        </el-table-column>
        <el-table-column label="IMP" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.IMP_date }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Produce" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Produce_date }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Sell" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Sell_date }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Close" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Close_date }}</span>
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column v-if="showRiskAction" label="Risk & Action" align="center">
        <el-table-column label="risk1" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Risk1 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="risk2" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Risk2 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="risk3" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Risk3 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="risk4" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Risk4 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Action1" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Action1 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Action2" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Action2 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Action3" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Action3 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Action4" width="100px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.Action4 }}</span>
          </template>
        </el-table-column>
      </el-table-column>
      <el-table-column align="center" label="Actions" width="100" fixed="right">
        <template slot-scope="scope">
          <router-link :to="'/PM/Project-Card-Info/edit/'+scope.row.id">
            <el-button type="primary" size="small" icon="el-icon-edit">
              Edit
            </el-button>
          </router-link>
        </template>
      </el-table-column>

    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

  </div>
</template>

<script>
import { fetchList, fetchPv, createCard, updateCard, deleteCard } from '@/api/card'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination/index'
import { fetch_search_list } from '@/api/project' // secondary package based on el-pagination
// import EditForm from '@./Project-Card-Info-edit'

export default {
  name: 'ProjectCardInfo',
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        Open: 'success',
        Deployment: 'info',
        Close: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        Current_status: undefined,
        Project_leader: undefined,
        Project_name: undefined,
        ordering: '+id'
      },
      showKPI: false, showRiskAction: false, showSchedule: false,
      orderingOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      project_name_list: null, statusOptions: null, leaderOptions: null, clusterOptions: null,
      regionOptions: ['North', 'South', 'Wuxi', 'East&West'],
      temp: {
        id: undefined,
        Region: 'North',
        Project_name: 'XSY Name',
        Project_leader: 'XSY',
        Project_type: 'PMP',
        Plant: 'Plant',
        Cluster: 'Cluster',
        Current_status: 'Open',
        Additional_COGS: '200',
        Space_needed: '20',
        Productivity: '30',
        CAPEX: '20',
        // importance: 1,
        remark: 'abcdef',
        // timestamp: new Date(),
        Workload_Date: '2021Q2',
        Workload: '0.5'
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        // Project_type: [{ required: true, message: 'type is required', trigger: 'change' }],
        timestamp: [{ type: 'date', required: true, message: 'timestamp is required', trigger: 'change' }],
        Project_name: [{ required: true, message: 'name is required', trigger: 'blur' }]
      },
      downloadLoading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = false
      fetchList(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total
      })
      fetch_search_list().then(response => {
        this.project_name_list = response.data.distinct_name
        this.leaderOptions = response.data.distinct_IPL
        this.clusterOptions = response.data.distinct_Cluster
        this.statusOptions = response.data.distinct_Current_status
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleModifyStatus(row, status) {
      this.$message({
        message: '操作Success',
        type: 'success'
      })
      row.status = status
    },
    orderingChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.orderingByID(order)
      }
    },
    orderingByID(order) {
      if (order === 'ascending') {
        this.listQuery.ordering = '+id'
      } else {
        this.listQuery.ordering = '-id'
      }
      this.handleFilter()
    },
    resetTemp() {
      this.temp = {
        id: undefined,
        Region: 'North',
        Project_name: 'XSY Name',
        Project_leader: 'XSY',
        Project_type: 'PMP',
        Current_status: 'Open',
        Plant: 'SSLVTA',
        Cluster: 'Cluster',
        Additional_COGS: '200',
        Space_needed: '20',
        Productivity: '30',
        CAPEX: '20',
        importance: 1,
        remark: 'blabla',
        timestamp: new Date()
      }
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.temp.author = 'vue-element-admin'
          createCard(this.temp).then(() => {
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Created Successfully',
              type: 'success',
              duration: 2000
            })
          }).catch(() => {
            this.$message({ type: 'warning', message: '请检查所填信息是否符合要求' })
          })
        }
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.temp.timestamp = new Date(this.temp.timestamp)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          tempData.timestamp = +new Date(tempData.timestamp) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
          updateCard(tempData, this.temp.id).then(() => {
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleDelete(row, index) {
      this.$confirm('你确定要删除该信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async() => {
        await deleteCard(row.id)
        // this.getList()
        this.$message({ type: 'success', message: '删除成功!' })
        this.list.splice(index, 1)
      }).catch(() => {
        this.$message({ type: 'success', message: '已取消删除' })
      })
    },
    handleFetchPv(pv) {
      fetchPv(pv).then(response => {
        this.pvData = response.data.pvData
        this.dialogPvVisible = true
      })
    },
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['timestamp', 'name', 'type', 'importance', 'status']
        const filterVal = ['timestamp', 'name', 'type', 'importance', 'status']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'table-list'
        })
        this.downloadLoading = false
      })
    },
    formatJson(filterVal) {
      return this.list.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    },
    getorderingClass: function(key) {
      const ordering = this.listQuery.ordering
      return ordering === `+${key}` ? 'ascending' : 'descending'
    }
  }
}

</script>
