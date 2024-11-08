<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            {{ title}}
        </div>
        <!-- <div class="mb-3">
            <u>Response data</u>:             
        </div> -->

        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addStationModal">
            Add Station
        </button>

        <!-- Modal -->
        <div class="modal fade" id="addStationModal" tabindex="-1" aria-labelledby="addStationModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addStationModalLabel">Add Station</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="newStation.name" type="text" class="form-control" id="name">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createStation" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>
        

        <StationTable
            :stations="stations"
            @delete-station="deleteStation"
            @edit-station="editStation"
        />

    </div>
  </template>
  
<script>
    import StationTable from '../components/StationTable.vue'

    const baseUrl = 'http://localhost:8000'

    export default {
        components: {
            StationTable
        },
        data() {
            return {
                title: 'London Tube',
                stations: [],
                newStation: {
                    name: '',
                    lines: []
                }
            }
        }, 
        async mounted() {
            const response = await fetch(`${baseUrl}/api/stations`)
            const data = await response.json()
            this.stations = data.stations;
        },

        methods: {
            async deleteStation(station) {
                if (confirm('Are you sure you want to delete this station?')) {
                    const response = await fetch(`${baseUrl}/api/station/${station.id}/`, {
                        method: 'DELETE'
                    })
                    if (response.ok) {
                        this.stations = this.stations.filter(s => s.id !== station.id)
                    }
                }
            },
            async createStation() {
                console.log(this.newStation)
                const response = await fetch(`${baseUrl}/api/stations/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.newStation)
                })
                const newStation = await response.json()
                this.stations.push(newStation)
            },
            async editStation(station) {
                const response = await fetch(`${baseUrl}/api/station/${station.id}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(station)
                })
                if (response.ok) {
                    const index = this.stations.findIndex(s => s.id === station.id)
                    this.stations.splice(index, 1, station)
                }
            }
        }
    }
</script>
