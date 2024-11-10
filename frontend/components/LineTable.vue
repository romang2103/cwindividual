<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Line</th>
                <th scope="col">Number of Stations</th>
                <th scope="col">Weekend Availability</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(line, index) in lines">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ line.name }}</td>
                <td>{{ line.numberOfStations }}</td>
                <td>{{ line.weekendAvailability ? 'Yes' : 'No'  }}</td>
                <td>
                    <button
                        class="btn btn-sm btn-primary me-2" 
                        data-bs-toggle="modal" 
                        data-bs-target="#editLineModal"
                        @click="selectLine(line)"
                    >
                        <i class="bi bi-pencil-square"></i>
                    </button>
                    <button
                        class="btn btn-sm btn-danger"
                        @click="$emit('delete-line', line)"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>

    <!-- Edit Line Modal -->
    <div class="modal fade" id="editLineModal" tabindex="-1" aria-labelledby="editLineModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="editLineModalLabel">Edit Line</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input v-model="updatedLine.name" type="text" class="form-control" id="name">
                    </div>
                    <div class="mb-3">
                        <label for="name" class="form-label">Number of Stations</label>
                        <input v-model="updatedLine.numberOfStations" type="text" class="form-control" id="numberOfStations">
                    </div>
                    <div class="mb-3">
                        <label for="name" class="form-label">Available on Weekends</label>
                        <select v-model="updatedLine.weekendAvailability" class="form-control" id="weekendAvailability">
                            <option :value="true">Yes</option>
                            <option :value="false">No</option>
                        </select>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="$emit('edit-line', updatedLine)" data-bs-dismiss="modal">Save</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        emits: ['delete-line', 'edit-line'],
        props: {
            lines: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                updatedLine: {
                    id: '',
                    name: '',
                    numberOfStations: '',
                    weekendAvailability: '',
                }
            }
        },
        methods: {
            selectLine(line) {
                this.updatedLine = { ...line }
                console.log(this.updatedLine)
            },
        }
    }

</script>