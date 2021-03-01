<template>
  <div class="app-container">
    <!--search bar-->
    <div class="filter-container">
      <el-input v-model="listQuery.Project_name" placeholder="Name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.Project_leader" placeholder="IPL" clearable style="width: 90px" class="filter-item">
        <el-option v-for="item in leaderOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.Current_status" placeholder="Stage" clearable style="width: 90px" class="filter-item">
        <el-option v-for="item in statusOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.Project_type" placeholder="Type" clearable class="filter-item" style="width: 130px">
        <el-option v-for="item in typeOptions" :key="item.key" :label="item.display_name" :value="item.key" />
      </el-select>
      <el-select v-model="listQuery.ordering" style="width: 140px" class="filter-item" @change="handleFilter">
        <el-option v-for="item in orderingOptions" :key="item.key" :label="item.label" :value="item.key" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" style="margin-left: 30px" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        Export
      </el-button>
      <!--      <el-checkbox v-model="showReviewer" class="filter-item" style="margin-left:15px;" @change="tableKey=tableKey+1">-->
      <!--        reviewer-->
      <!--      </el-checkbox>-->
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
      <el-table-column label="ID" prop="id" orderingable="custom" align="center" width="80" :class-name="getorderingClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <!--      <el-table-column label="Date" width="150px" align="center">-->
      <!--        <template slot-scope="{row}">-->
      <!--          <span>{{ row.timestamp | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>-->
      <!--        </template>-->
      <!--      </el-table-column>-->
      <el-table-column label="Name" min-width="100px">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.Project_name }}</span>
          <!--          <el-tag>{{ row.Project_type | typeFilter }}</el-tag>-->
        </template>
      </el-table-column>
      <el-table-column label="Stage" class-name="status-col" width="100">
        <template slot-scope="{row}">
          <el-tag :type="row.Current_status | statusFilter">
            {{ row.Current_status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="Leader" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Project_leader }}</span>
        </template>
      </el-table-column>
      <el-table-column label="COGS" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Additional_COGS }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Space" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Space_needed }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Prod" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Additional_COGS }}</span>
        </template>
      </el-table-column>
      <el-table-column label="CAPEX" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.CAPEX }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Type" width="110px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Project_type }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Region" width="110px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Region }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Cluster" width="110px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.Cluster }}</span>
        </template>
      </el-table-column>
      <!--      <el-table-column v-if="showReviewer" label="Reviewer" width="110px" align="center">-->
      <!--        <template slot-scope="{row}">-->
      <!--          <span style="color:red;">{{ row.reviewer }}</span>-->
      <!--        </template>-->
      <!--      </el-table-column>-->
      <!--      <el-table-column label="Imp" width="80px">-->
      <!--        <template slot-scope="{row}">-->
      <!--          <svg-icon v-for="n in + row.importance" :key="n" icon-class="star" class="meta-item__icon" />-->
      <!--        </template>-->
      <!--      </el-table-column>-->
      <!--      <el-table-column label="Readings" align="center" width="95">-->
      <!--        <template slot-scope="{row}">-->
      <!--          <span v-if="row.pageviews" class="link-type" @click="handleFetchPv(row.pageviews)">{{ row.pageviews }}</span>-->
      <!--          <span v-else>0</span>-->
      <!--        </template>-->
      <!--      </el-table-column>-->

      <el-table-column label="Actions" align="center" width="230" class-name="small-padding fixed-width">
        <template slot-scope="{row,$index}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            Edit
          </el-button>
          <!--          <el-button v-if="row.status!='draft'" size="mini" @click="handleModifyStatus(row,'draft')">-->
          <!--            Draft-->
          <!--          </el-button>-->
          <el-button v-if="row.Current_status!='deleted'" size="mini" type="danger" @click="handleDelete(row,$index)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 600px; margin-left:50px;">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="Name" prop="name">
              <el-input v-model="temp.Project_name" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Leader" prop="leader">
              <el-input v-model="temp.Project_leader" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="Region">
              <el-select v-model="temp.Region" class="filter-item" placeholder="Please select">
                <el-option v-for="item in regionOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Cluster">
              <el-select v-model="temp.Cluster" class="filter-item" placeholder="Please select">
                <el-option v-for="item in clusterOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="Type">
              <el-select v-model="temp.Project_type" class="filter-item" placeholder="Please select">
                <el-option v-for="item in typeOptions" :key="item.key" :label="item.display_name" :value="item.key" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Stage">
              <el-select v-model="temp.Current_status" class="filter-item" placeholder="Please select">
                <el-option v-for="item in statusOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
          <!--          <el-col span="12">-->
          <!--            <el-form-item label="Date" prop="timestamp">-->
          <!--          <el-date-picker v-model="temp.timestamp" type="datetime" placeholder="Please pick a date" />-->
          <!--        </el-form-item>-->
          <!--          </el-col>-->
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="COGS">
              <el-input v-model="temp.Additional_COGS" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Space" prop="leader">
              <el-input v-model="temp.Space_needed" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="Prod">
              <el-input v-model="temp.Productivity" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="CAPEX" prop="leader">
              <el-input v-model="temp.CAPEX" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item label="Remark">
          <el-input v-model="temp.remark" :autosize="{ minRows: 2, maxRows: 4}" type="textarea" placeholder="Please input" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="dialogPvVisible" name="Reading statistics">
      <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
        <el-table-column prop="key" label="Channel" />
        <el-table-column prop="pv" label="Pv" />
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogPvVisible = false">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { fetchList, fetchPv, createArticle, updateArticle, deleteDictDetail } from '@/api/article'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

const typeOptions = [
  { key: 'PMP', display_name: 'PMP' },
  { key: 'PEP/PWP', display_name: 'PEP/PWP' },
  { key: 'Rebalancing/Transfer', display_name: 'Reb/Tran' },
  { key: 'Others', display_name: 'Others' }
]

// arr to obj, such as { CN : "China", US : "USA" }
const calendarTypeKeyValue = typeOptions.reduce((acc, cur) => {
  acc[cur.key] = cur.display_name
  return acc
}, {})

export default {
  name: 'ComplexTable',
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
    },
    typeFilter(type) {
      return calendarTypeKeyValue[type]
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
        Project_type: undefined,
        Project_name: undefined,
        ordering: '+id'
      },
      importanceOptions: [1, 2, 3],
      typeOptions,
      orderingOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      statusOptions: ['Open', 'Deployment', 'Produce', 'Close'],
      leaderOptions: ['Pan Wen', 'HuLin-Alex Cai'],
      clusterOptions: ['MTOMTS'],
      regionOptions: ['North', 'South', 'Wuxi', 'East&West'],
      showReviewer: false,
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
        importance: 1,
        remark: 'abcdef',
        timestamp: new Date()
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
        Project_type: [{ required: true, message: 'type is required', trigger: 'change' }],
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
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
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
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.temp.author = 'vue-element-admin'
          createArticle(this.temp).then(() => {
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
          updateArticle(tempData, this.temp.id).then(() => {
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
        await deleteDictDetail(row.id)
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

