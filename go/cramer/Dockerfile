FROM golang:1.26-alpine AS build
WORKDIR /app
#COPY go.mod go.sum .
COPY go.mod .
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /main .
RUN chmod +x /main

FROM scratch AS binary
COPY --from=build /main /main
ENTRYPOINT ["/main"]

