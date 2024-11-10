<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            {{ title}}
        </div>
        <!-- <div class="mb-3">
            <u>Response data</u>:             
        </div> -->

        <!-- Navigation bar -->
        <nav>
            <div class="nav nav-tabs" id="nav-tab" role="tablist">
                <button class="nav-link active" id="nav-stations-tab" data-bs-toggle="tab" data-bs-target="#nav-stations" type="button" role="tab" aria-controls="nav-stations" aria-selected="true">Stations</button>
                <button class="nav-link" id="nav-lines-tab" data-bs-toggle="tab" data-bs-target="#nav-lines" type="button" role="tab" aria-controls="nav-lines" aria-selected="false">Lines</button>
            </div>
        </nav>

        <div class="tab-content" id="nav-tabContent">
            <div class="tab-pane fade show active" id="nav-stations" role="tabpanel" aria-labelledby="nav-stations-tab">
                <!-- Button trigger modal -->
                <button type="button" class="btn btn-primary m-3" data-bs-toggle="modal" data-bs-target="#addStationModal">
                    Add Station
                </button>

                <!-- Station Table -->
                <StationTable
                    :stations="stations"
                    @delete-station="deleteStation"
                    @edit-station="editStation"
                />
            </div>
            <div class="tab-pane fade" id="nav-lines" role="tabpanel" aria-labelledby="nav-lines-tab">
                <!-- Button trigger modal -->
                <button type="button" class="btn btn-primary m-3" data-bs-toggle="modal" data-bs-target="#addLineModal">
                    Add Line
                </button>

                <LineTable
                    :lines="lines"
                    @delete-line="deleteLine"
                    @edit-line="editLine"
                />
            </div>
        </div>

        <!-- Add Station Modal -->
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

        <!-- Add Line Modal -->
        <div class="modal fade" id="addLineModal" tabindex="-1" aria-labelledby="addLineModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addLineModalLabel">Add Line</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="newLine.name" type="text" class="form-control" id="name">
                        </div>
                        <div class="mb-3">
                            <label for="name" class="form-label">Number of Stations</label>
                            <input v-model="newLine.numberOfStations" type="text" class="form-control" id="numberOfStations">
                        </div>
                        <div class="mb-3">
                            <label for="name" class="form-label">Available on Weekends</label>
                            <select v-model="newLine.weekendAvailability" class="form-control" id="weekendAvailability">
                                <option :value="true">Yes</option>
                                <option :value="false">No</option>
                            </select>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createLine" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>
        

        <!-- <StationTable
            :stations="stations"
            @delete-station="deleteStation"
            @edit-station="editStation"
        /> -->

    </div>
  </template>
  
<script>
    import StationTable from '../components/StationTable.vue'
    import LineTable from '../components/LineTable.vue'

    const baseUrl = 'http://localhost:8000'

    export default {
        components: {
            StationTable,
            LineTable
        },
        data() {
            return {
                title: 'London Tube',
                stations: [],
                newStation: {
                    name: '',
                    lines: []
                },
                lines: [],
                newLine: {
                    name: '',
                    numberOfStations: '',
                    weekendAvailability: '',
                }
            }
        }, 
        async mounted() {
            const stations_response = await fetch(`${baseUrl}/api/stations`)
            const stations_data = await stations_response.json()
            this.stations = stations_data.stations;

            const lines_response = await fetch(`${baseUrl}/api/lines`)
            const lines_data = await lines_response.json()
            console.log("Lines data: ", lines_data);
            console.log(lines_data.lines);
            this.lines = lines_data.lines;
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
            async deleteLine(line) {
                console.log('delete line', line)
                if (confirm('Are you sure you want to delete this line?')) {
                    const response = await fetch(`${baseUrl}/api/line/${line.id}/`, {
                        method: 'DELETE'
                    })
                    if (response.ok) {
                        this.lines = this.lines.filter(l => l.id !== line.id)
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
            },
            async editLine(line) {
                const response = await fetch(`${baseUrl}/api/line/${line.id}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(line)
                })
                if (response.ok) {
                    const index = this.lines.findIndex(l => l.id === line.id)
                    this.lines.splice(index, 1, line)
                }
            },
            async createLine() {
                const response = await fetch(`${baseUrl}/api/lines/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.newLine)
                })
                const newLine = await response.json()
                this.lines.push(newLine)
            }
        }
    }
</script>
