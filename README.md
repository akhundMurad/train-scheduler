# Trains Schedule Management Service

## Project description

This service is responsible for managing train schedules. The main purpose of this repository is to demonstrate the implementation of multiple complex patterns.

## Business Logic

This section provides an overview of the main business rules and processes that drive the project.

### Commands and Events

#### Events

- Train booked: This event could be triggered when a customer books a train ticket, which would then initiate the train scheduling process.

- Train departed: This event could be triggered when a train departs from a station, which would then update the train's status and trigger subsequent events.

- Train arrived: This event could be triggered when a train arrives at a station, which would then update the train's status and trigger subsequent events.

- Delay reported: This event could be triggered when a delay is reported for a train, which would then initiate the process of managing the delay and updating the train schedule.

#### Commands

- Schedule train: This command could be triggered when a train operator schedules a train, which would then add the train to the schedule and trigger subsequent events.

- Approve delay: This command could be triggered when a designated authority approves a delay, which would then update the train schedule and notify the relevant parties.

- Report delay: This command could be triggered when a designated authority approves a delay.

- Update train status: This command could be triggered when a train's status changes, which would then update the train schedule and notify the relevant parties.

- Dispatch train: This command could be triggered when a train is ready to depart from a station, which would then update the train's status and notify the relevant parties.

#### Possible train statuses

- Scheduled: This status indicates that a train has been scheduled for a specific route and time.

- Departed: This status indicates that a train has departed from its origin station and is en route to its destination.

- Arrived: This status indicates that a train has arrived at its destination station and has completed its journey.

- Delayed: This status indicates that a train is running behind schedule due to various reasons, such as weather conditions or mechanical issues.

- Cancelled: This status indicates that a train has been cancelled for some reason and will not run on its scheduled route.

## License

This project is licensed under the terms of the MIT license.
